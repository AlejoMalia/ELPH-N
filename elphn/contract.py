# -*- coding: utf-8 -*-
"""The agreement contract: does what arrived agree with what departed?"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Sequence

import numpy as np

from .evidence import Status, formula

__all__ = ["disagreement", "band", "dead_zone", "contract_holds", "far_bound",
           "decidability", "materiality", "Verdict"]


@formula(number=1, name="Disagreement", expression="omega = 1 - corr",
         units="dimensionless", status=Status.MEAS_PRO, source="D-370",
         domain=lambda corr: ("correlation must lie in [-1, 1]"
                              if not -1.0 <= float(corr) <= 1.0 else None),
         domain_text="-1 <= corr <= 1")
def disagreement(corr: float) -> float:
    """Disagreement between two readings of the same closed volume."""
    return 1.0 - float(corr)


@formula(number=2, name="Band", expression="A = sqrt(omega_impostor / omega_act)",
         units="dimensionless", status=Status.MEAS_PRO, source="D-663",
         domain=lambda om_imp, om_act: (
             "omega_act must be > 0" if om_act <= 0 else
             "omega_impostor must be > 0" if om_imp <= 0 else None),
         domain_text="both omegas > 0; omega_impostor is the NEAREST impostor, not the median")
def band(om_impostor: float, om_act: float) -> float:
    """Band against the **nearest** impostor.

    Taking the median of the impostor distribution flatters the band; the tail is what
    matters, exactly as in biometric practice. Passing a median here is not detectable
    by this function — it is the caller's responsibility, and it was a real defect of
    the engine until D-663.
    """
    return math.sqrt(float(om_impostor) / float(om_act))


@formula(number=3, name="Dead zone", expression="dA/A = 0.5*sqrt(u_imp^2 + u_act^2)",
         units="dimensionless (relative)", status=Status.DER, source="D-663",
         domain=lambda u_imp, u_act: ("relative uncertainties must be >= 0"
                                      if min(u_imp, u_act) < 0 else None),
         domain_text="u >= 0, expressed as relative uncertainties")
def dead_zone(u_impostor: float, u_act: float) -> float:
    """Relative half-width below which a band is a tie, not a contract.

    With u = 10 % on both, A in [0.934, 1.071] is a **tie**. Reporting A = 1.05 as a
    contract, which the engine did before D-663, is reporting a coin flip.
    """
    return 0.5 * math.sqrt(float(u_impostor) ** 2 + float(u_act) ** 2)


@dataclass(frozen=True)
class Verdict:
    """The outcome of a contract evaluation."""
    band: float
    dead_zone: float
    threshold: float
    holds: bool
    reason: str

    def __bool__(self) -> bool:
        return self.holds

    def __str__(self) -> str:  # pragma: no cover
        return (f"A = {self.band:.3f}  threshold = {self.threshold:.3f}  "
                f"-> {'CONTRACT' if self.holds else 'NO CONTRACT'} ({self.reason})")


@formula(name="Contract rule", expression="contract exists  <=>  A > 1 + dA",
         units="dimensionless", status=Status.DER, source="D-663",
         domain_text="requires a dead zone; A > 1 alone is not a contract")
def contract_holds(om_impostor: float, om_act: float,
                   u_impostor: float = 0.10, u_act: float = 0.10) -> Verdict:
    """Evaluate the contract, dead zone included.

    >>> v = contract_holds(4.993e-2, 8.16e-4)      # the measured act
    >>> bool(v), round(v.band, 2)
    (True, 7.82)
    >>> bool(contract_holds(1.10e-3, 1.0e-3))      # a tie, not a contract
    False
    """
    A = band(om_impostor, om_act)
    dA = dead_zone(u_impostor, u_act)
    thr = 1.0 + dA
    holds = A > thr
    return Verdict(A, dA, thr,
                   holds, "above the dead zone" if holds else "inside the dead zone: a tie")


@formula(number=4, name="False acceptance bound (rule of three)",
         expression="FAR <= 3/k  when zero acceptances are observed in k trials",
         units="dimensionless (rate)", status=Status.LIT,
         source="Hanley & Lippman-Hand 1983",
         domain=lambda k, acceptances=0: (
             "k must be >= 1" if k < 1 else
             "the rule of three applies only to ZERO observed acceptances; "
             "with acceptances > 0 use an exact binomial interval"
             if acceptances else None),
         domain_text="k >= 1 and zero observed acceptances")
def far_bound(k: int, acceptances: int = 0) -> float:
    """Upper bound on a rate that was never observed to occur.

    **A rate without its k says nothing.** Zero deaths in 37 acts does not mean zero:
    it means at most one in twelve.

    >>> far_bound(3_000_000)
    1e-06
    >>> round(far_bound(37), 4)
    0.0811
    """
    return 3.0 / float(k)


@formula(number=5, name="Decidability index",
         expression="d' = |mu_I - mu_G| / sqrt((sigma_I^2 + sigma_G^2)/2)",
         units="dimensionless (sigmas)", status=Status.LIT, source="Daugman 2006",
         domain=lambda mu_i, mu_g, s_i, s_g: ("standard deviations must be > 0"
                                              if min(s_i, s_g) <= 0 else None),
         domain_text="sigma > 0 for both distributions")
def decidability(mu_impostor: float, mu_genuine: float,
                 sd_impostor: float, sd_genuine: float) -> float:
    """Separation between the genuine and impostor distributions, in sigmas."""
    return abs(mu_impostor - mu_genuine) / math.sqrt(
        (sd_impostor ** 2 + sd_genuine ** 2) / 2.0)


@formula(number=8, name="Instantaneous-certified exclusion",
         expression="psi = g * K^4 / A^4", units="dimensionless",
         status=Status.DER, source="D-605",
         domain=lambda g, K, A: ("A must be > 0" if A <= 0 else
                                 "g must be > 0" if g <= 0 else None),
         domain_text="g > 0, A > 0")
def materiality(g: float, K: float, A: float) -> float:
    """How far the act is from being informational rather than material.

    ``psi = 1`` is the boundary. The published act (g = 3, K3 = 0.597, A = 7.80) sits
    at 1.03e-4: the act is **9,713 times more material than informational**.

    Note the band constant: ``K3 = 0.597`` is the one used for the published figure.
    Substituting ``K2 = 0.632`` gives 7,813, which is a different claim about a
    different symmetry group, not a rounding difference.

    >>> round(materiality(3.0, 0.597, 7.80), 7)
    0.000103
    >>> round(1 / materiality(3.0, 0.597, 7.80))
    9713
    """
    return float(g) * float(K) ** 4 / float(A) ** 4
