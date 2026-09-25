# -*- coding: utf-8 -*-
"""Scale laws, and the ceiling that ends the discussion about carrying 100 people.

Two effects pull in opposite directions: ``Omega ~ 1/L`` makes a larger cabin *easier*
to certify, while ``alpha`` decreasing with ``L`` makes GATE-0 *impossible*. Where the
field's own disagreement overtakes the detection floor, there is nothing left to
certify — and that crossing is a number, not an opinion.
"""
from __future__ import annotations

import math

from .evidence import Status, formula

__all__ = ["bubble_ceiling", "seats_for", "wall_thickness", "shell_mass",
           "energy_per_person", "DETECTION_FLOOR_MM", "VOLUME_PER_PERSON_M3"]

DETECTION_FLOOR_MM = 1.0       # what the machine can resolve, at 90 % power
VOLUME_PER_PERSON_M3 = 14.1    # the 3 m cabin, which gives the 15.8 min CO2 clock
MIN_WALL_MM = {"steel": 4.0, "aluminium": 6.5, "composite": 7.5}   # for a 3 m cabin


@formula(name="Bubble ceiling",
         expression="L_max = detection_floor / (D(r0)/r0)   [alpha = 1]",
         units="m", status=Status.DER, source="D-712",
         domain=lambda d_ref_um=35.0, r0_mm=176.0, floor_mm=DETECTION_FLOOR_MM: (
             "all arguments must be > 0"
             if min(d_ref_um, r0_mm, floor_mm) <= 0 else None),
         domain_text="all > 0; assumes alpha = 1, i.e. disagreement linear in separation")
def bubble_ceiling(d_ref_um: float = 35.0, r0_mm: float = 176.0,
                   floor_mm: float = DETECTION_FLOOR_MM) -> float:
    """Largest shell that can still be certified, in metres.

    With alpha = 1 the field's disagreement grows **linearly** with size and the
    detection floor does not. Above the crossing, a real 1 mm defect is
    indistinguishable from the field's own disagreement.

    >>> round(bubble_ceiling(), 2)
    5.03
    """
    slope_um_per_mm = d_ref_um / r0_mm
    return (floor_mm * 1000.0 / slope_um_per_mm) / 1000.0


@formula(name="Seats for a given shell",
         expression="N = (pi/6) L^3 / volume_per_person", units="persons",
         status=Status.DER, source="D-712",
         domain=lambda length_m, per_person_m3=VOLUME_PER_PERSON_M3: (
             "length and volume per person must be > 0"
             if min(length_m, per_person_m3) <= 0 else
             f"{length_m:.2f} m exceeds the certifiable ceiling of "
             f"{bubble_ceiling():.2f} m" if length_m > bubble_ceiling() else None),
         domain_text="0 < L <= the bubble ceiling (5.03 m)")
def seats_for(length_m: float, per_person_m3: float = VOLUME_PER_PERSON_M3) -> int:
    """How many occupants a spherical cabin of this size admits.

    >>> seats_for(bubble_ceiling())    # exactly at the ceiling
    4
    >>> seats_for(3.0)
    1
    """
    volume = math.pi / 6.0 * length_m ** 3
    return int(volume // per_person_m3)


@formula(number=31, name="Wall thickness", expression="t_wall proportional to L",
         units="mm", status=Status.DER, source="D-674",
         domain=lambda length_m, material="steel": (
             f"unknown material {material!r}; choose from {sorted(MIN_WALL_MM)}"
             if material not in MIN_WALL_MM else
             "length must be > 0" if length_m <= 0 else None),
         domain_text="material in {steel, aluminium, composite}; L > 0")
def wall_thickness(length_m: float, material: str = "steel") -> float:
    """Minimum wall for a pressure shell of this size.

    >>> wall_thickness(3.0)
    4.0
    """
    return MIN_WALL_MM[material] * length_m / 3.0


@formula(number=32, name="Shell mass", expression="M proportional to L^3",
         units="kg", status=Status.DER, source="D-674",
         domain=lambda length_m, reference_kg=888.0, reference_m=3.0: (
             "all arguments must be > 0"
             if min(length_m, reference_kg, reference_m) <= 0 else None),
         domain_text="all > 0")
def shell_mass(length_m: float, reference_kg: float = 888.0,
               reference_m: float = 3.0) -> float:
    """Shell mass by the cube law.

    >>> round(shell_mass(3.0))
    888
    >>> round(shell_mass(0.3))
    1
    """
    return reference_kg * (length_m / reference_m) ** 3


@formula(name="Energy per occupant", expression="E/N is FLAT, because E ~ L^3 ~ N",
         units="J per person", status=Status.DER, source="D-712",
         domain=lambda n_persons, distance_m, g=1.0, per_person_kg=1000.0: (
             "n_persons must be >= 1" if n_persons < 1 else
             "distance must be > 0" if distance_m <= 0 else None),
         domain_text="n >= 1; distance > 0")
def energy_per_person(n_persons: int, distance_m: float, g: float = 1.0,
                      per_person_kg: float = 1000.0) -> float:
    """Transit energy divided by occupants — and it does not fall.

    **There is no economy of scale.** Moving 100 people together costs exactly what 100
    single acts cost, so splitting them across many small shells loses nothing. This is
    why the 5.03 m ceiling does not matter operationally.

    >>> a = energy_per_person(1, 930e3)
    >>> b = energy_per_person(4, 930e3)
    >>> abs(a - b) < 1e-9
    True
    """
    from .kinematics import transit_energy
    total_mass = per_person_kg * n_persons
    return transit_energy(total_mass, distance_m, g=g) / n_persons
