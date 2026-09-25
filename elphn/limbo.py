# -*- coding: utf-8 -*-
"""Limbos: intervals during which a guarantee is suspended.

The most transferable idea in the framework, and the one least tied to its premise.
A limbo is any window in which something is in neither of its two defined states and
no party controls it. Surgery has them (cross-clamp time), launch has them (black
zones), banking has them (the Herstatt window), aviation has them (past V1).

The finding that generalises: **the most dangerous limbo is the shortest one.**
Ordering by duration and ordering by danger came out inverse, because duration is
what everyone measures and mitigation is what nobody does.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .evidence import Status, formula

__all__ = ["Limbo", "limbo_risk", "elasticity", "total_exposure"]


@dataclass(frozen=True)
class Limbo:
    """A window with a guarantee suspended.

    ``p_mitigation = 0`` is not a modelling convenience: it is the honest value for a
    phase with no controller, and writing it as anything else is how such phases get
    quietly costed away.
    """
    name: str
    minutes: float
    p_event: float
    p_mitigation: float = 0.0
    controller: str = ""

    def __post_init__(self) -> None:
        if self.minutes < 0:
            raise ValueError(f"{self.name}: duration must be >= 0")
        for label, p in (("p_event", self.p_event), ("p_mitigation", self.p_mitigation)):
            if not 0.0 <= p <= 1.0:
                raise ValueError(f"{self.name}: {label} must lie in [0, 1]")

    @property
    def risk(self) -> float:
        return limbo_risk(self.minutes, self.p_event, self.p_mitigation)

    @property
    def mitigated(self) -> bool:
        return self.p_mitigation > 0.0


@formula(number=40, name="Limbo risk",
         expression="risk(L) = duration * P(event) * (1 - P(mitigation))",
         units="risk-equivalent minutes", status=Status.DER, source="D-705",
         domain=lambda minutes, p_event, p_mitigation=0.0: (
             "duration must be >= 0" if minutes < 0 else
             "probabilities must lie in [0, 1]"
             if not (0 <= p_event <= 1 and 0 <= p_mitigation <= 1) else None),
         domain_text="duration >= 0; probabilities in [0, 1]")
def limbo_risk(minutes: float, p_event: float, p_mitigation: float = 0.0) -> float:
    """Exposure contributed by one limbo.

    >>> round(limbo_risk(3.4, 0.01, 0.0), 3)     # transit: null mitigation
    0.034
    >>> round(limbo_risk(34.0, 0.01, 0.9), 3)    # ten times longer, well mitigated
    0.034
    """
    return minutes * p_event * (1.0 - p_mitigation)


@formula(number=42, name="Total exposure", expression="E = sum of risk(L_i)",
         units="risk-equivalent minutes", status=Status.DER, source="D-718",
         domain_text="an UPPER BOUND, not the exposure: limbos overlap (L1 with L3), "
                     "and summing them as disjoint overestimates")
def total_exposure(limbos: Iterable[Limbo]) -> float:
    """Sum of limbo risks.

    Reported as a bound rather than a value because the limbos are **not disjoint**.
    """
    return sum(l.risk for l in limbos)


@formula(number=43, name="Limbo elasticity",
         expression="e(L, x) = (dL/L) / (dx/x)", units="dimensionless",
         status=Status.DER, source="D-707",
         domain=lambda l0, l1, x0, x1: (
             "baseline duration and driver must be > 0" if min(l0, x0) <= 0 else
             "the driver must change" if x1 == x0 else None),
         domain_text="l0, x0 > 0 and x1 != x0")
def elasticity(l0: float, l1: float, x0: float, x1: float) -> float:
    """How far a limbo stretches when a driver — route, load, time — changes.

    A negative elasticity would mean that lengthening the route shortens the limbo,
    which is impossible by construction for the transit limbo: it grows with route.

    >>> round(elasticity(3.4, 6.8, 930.0, 3720.0), 3)
    0.333
    """
    return ((l1 - l0) / l0) / ((x1 - x0) / x0)
