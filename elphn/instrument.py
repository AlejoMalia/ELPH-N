# -*- coding: utf-8 -*-
"""The reader, and GATE-0 — the veto the whole architecture hangs from.

GATE-0 asks one question of a pair of nominally identical parts:

    does the disagreement between them GROW with separation?

    D(r) = C * r^alpha

    alpha ~ 1    smooth field        -> a local affine kills it as (r/L)^2.   PASS
    alpha ~ 0.5  random walk         -> only sqrt(r/L).                       INTERMEDIATE
    alpha ~ 0    independent by site -> the reference hierarchy does not work. VETO

The rule is deliberately asymmetric and says so: **a reliable veto (98.7 %) and a poor
pass (46 %)**. A test honest about which of its two answers to trust is rarer than it
should be.
"""
from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from typing import Optional, Sequence, Tuple

import numpy as np

from .evidence import Status, formula

__all__ = ["structure_exponent", "gate0", "Gate0Result", "pct_inv",
           "dynamic_threshold", "floor_noise", "D0_MAX_UM", "R0_MM"]

R0_MM = 176.0      # reference separation: the diameter of the useful field
D0_MAX_UM = 35.0   # the residue the budget allows at that separation
SUELO_REL = 1e-9   # relative floor: D/r below this is a perfect field, not missing data


def _theil_sen(x: np.ndarray, y: np.ndarray) -> Tuple[float, float]:
    """Theil-Sen slope and intercept. Breakdown point 29.3 %.

    Ordinary least squares has breakdown 1/n, and a single contaminated fiducial — a
    50 um speck on 25 — dragged alpha from 0.974 to 0.765, turning PASS into
    INTERMEDIATE. scipy is used when present; this fallback keeps the package
    dependency-light and gives the same answer.
    """
    try:
        from scipy.stats import theilslopes
        a, b = theilslopes(y, x)[:2]
        return float(a), float(b)
    except ImportError:
        pass
    n = len(x)
    slopes = [(y[j] - y[i]) / (x[j] - x[i])
              for i, j in itertools.combinations(range(n), 2) if x[j] != x[i]]
    a = float(np.median(slopes))
    return a, float(np.median(y - a * x))


@formula(number=14, name="Structure function", expression="D(r) = C * r^alpha",
         units="alpha dimensionless; C in [length]*[length]^-alpha",
         status=Status.MEAS_PRO, source="D-669",
         domain=lambda pa, pb: (
             "the two point sets must have the same shape"
             if np.shape(pa) != np.shape(pb) else
             "at least 4 matched fiducials are required" if len(pa) < 4 else None),
         domain_text="matched point sets, >= 4 fiducials. NOTE: alpha is a FITTED "
                     "parameter, so the units of C change with every fit and a fixed "
                     "threshold on C is not dimensionally valid — judge D(r0) instead")
def structure_exponent(points_a: Sequence[Sequence[float]],
                       points_b: Sequence[Sequence[float]]
                       ) -> Tuple[float, float, float, int]:
    """Fit ``D(r) = C*r^alpha`` over every pair. Returns ``(alpha, C, R2, n_pairs)``.

    The common translation is removed first: that is not a disagreement, it is where
    the part was placed. Lens distortion is likewise common-mode and cancels in the
    difference **provided the camera did not move between the two photographs** — the
    single hardest requirement of the bench protocol.
    """
    A = np.asarray(points_a, dtype=float)
    B = np.asarray(points_b, dtype=float)
    A = A - A.mean(0)
    B = B - B.mean(0)
    i, j = np.triu_indices(len(A), 1)
    r = np.linalg.norm(A[i] - A[j], axis=1)
    D = np.linalg.norm((A[i] - A[j]) - (B[i] - B[j]), axis=1)
    ok = (r > 0) & (D > SUELO_REL * r)
    if (r > 0).sum() >= 3 and ok.sum() < 3:
        # A field below the reader's floor is not missing data: it is a perfectly
        # smooth field, and that is alpha = 1 by construction. Returning NaN here
        # made the instrument fail in the BEST possible case (D-693).
        return 1.0, float(np.median(D[r > 0])), 1.0, int((r > 0).sum())
    if ok.sum() < 3:
        return float("nan"), float("nan"), 0.0, int(ok.sum())
    x, y = np.log(r[ok]), np.log(D[ok])
    a, b = _theil_sen(x, y)
    ss_res = float(((y - (a * x + b)) ** 2).sum())
    ss_tot = max(float(((y - y.mean()) ** 2).sum()), 1e-30)
    return float(a), float(math.exp(b)), 1.0 - ss_res / ss_tot, int(ok.sum())


@dataclass(frozen=True)
class Gate0Result:
    alpha: float
    C: float
    r_squared: float
    n_pairs: int
    d_ref_um: float
    verdict: str

    def __str__(self) -> str:  # pragma: no cover
        return (f"alpha = {self.alpha:.3f}   D({R0_MM:.0f} mm) = {self.d_ref_um:.1f} um"
                f"   R2 = {self.r_squared:.3f}   pairs = {self.n_pairs}\n{self.verdict}")


@formula(number=16, name="GATE-0 decision rule",
         expression="VETO if alpha < 0.35; PASS if alpha >= 0.95 AND D(176 mm) <= 35 um",
         units="alpha dimensionless; D in um", status=Status.MEAS_PRO, source="D-649/D-669",
         domain_text="the rule is JOINT: smoothness AND amplitude. A reliable veto "
                     "(98.7 %) and a poor pass (46 %)")
def gate0(points_a: Sequence[Sequence[float]], points_b: Sequence[Sequence[float]],
          units_mm: bool = True) -> Gate0Result:
    """Run GATE-0 on two matched fiducial sets.

    ``units_mm`` says the coordinates are in millimetres, so that ``D(r0)`` can be
    reported in micrometres.
    """
    alpha, C, r2, n = structure_exponent(points_a, points_b)
    if not math.isfinite(alpha):
        return Gate0Result(alpha, C, r2, n, float("nan"), "NO DATA")
    d0 = C * (1e3 if units_mm else 1.0) * R0_MM ** alpha
    if alpha < 0.35:
        v = ("VETO - error independent by site: the reference hierarchy does not work "
             "(reliable at 98.7 %)")
    elif alpha >= 0.95 and d0 <= D0_MAX_UM:
        v = "PASS - smooth field AND amplitude within budget"
    elif alpha >= 0.95:
        v = f"INTERMEDIATE - alpha holds but D({R0_MM:.0f} mm) = {d0:.1f} um > {D0_MAX_UM:.0f}"
    else:
        v = "INTERMEDIATE - not sufficient to launch the act"
    return Gate0Result(alpha, C, r2, n, d0, v)


@formula(number=11, name="Inventory percentile", expression="PCT_INV = 100*(1 - 1/(2n))",
         units="percent", status=Status.DER, source="D-665",
         domain=lambda n: "n must be >= 2" if n < 2 else None,
         domain_text="n >= 2. A percentile fixed independently of n misstates the power")
def pct_inv(n: int) -> float:
    """The percentile that the largest of ``n`` samples actually represents.

    A fixed p98 threshold with n = 50 detected **10 %** of the cases where 90 % had
    been declared. Tie the percentile to the sample size.

    >>> round(pct_inv(50), 1)
    99.0
    >>> round(pct_inv(10), 1)
    95.0
    """
    return 100.0 * (1.0 - 1.0 / (2.0 * n))


@formula(number=9, name="Dynamic threshold",
         expression="delta = K*(sigma_floor/mu_floor)*sqrt(2);  threshold = (1+delta)*floor",
         units="same as the floor", status=Status.DER, source="D-608",
         domain=lambda floor, sd_floor, mean_floor, k=3.0: (
             "mean_floor must be > 0" if mean_floor <= 0 else
             "sd_floor must be >= 0" if sd_floor < 0 else None),
         domain_text="mean_floor > 0. The sqrt(2) is because origin and destination "
                     "are two independent measurements and the variances add")
def dynamic_threshold(floor: float, sd_floor: float, mean_floor: float,
                      k: float = 3.0) -> float:
    """Acceptance threshold scaled to the measured floor and its scatter."""
    delta = k * (sd_floor / mean_floor) * math.sqrt(2.0)
    return (1.0 + delta) * floor


@formula(number=10, name="Floor noise", expression="relative error = 1/sqrt(2(n-1))",
         units="dimensionless (relative)", status=Status.DER, source="regla 413",
         domain=lambda n: "n must be >= 2" if n < 2 else None,
         domain_text="n >= 2. The floor is measured by RE-PLACING the part, not by "
                     "re-photographing it")
def floor_noise(n: int) -> float:
    """Relative uncertainty of a floor estimated from ``n`` re-placements.

    >>> round(floor_noise(10), 3)
    0.236
    >>> round(floor_noise(50), 3)
    0.101
    """
    return 1.0 / math.sqrt(2.0 * (n - 1))
