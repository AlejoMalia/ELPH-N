# -*- coding: utf-8 -*-
"""Transit kinematics, and the two ceilings that bound them.

Two limits are enforced here rather than documented, because both were discovered by
calling the formulas outside the range their authors had checked:

* the transit-time law assumes continuous accelerate/decelerate, so its peak velocity
  grows as ``sqrt(a*d)`` and **exceeds Earth escape velocity at 1,421 km for 9 g**.
  Past that the profile is not a hop but a departure, and the law does not model the
  coast phase it would need (D-713);
* stagnation heating grows as ``v^3``, and the shell must stay below the creep
  threshold for its form certificate to survive, which sets a **maximum velocity per
  altitude** (D-717).
"""
from __future__ import annotations

import math

from .evidence import Status, formula

__all__ = ["G0", "V_ESCAPE", "transit_time", "peak_velocity", "max_range",
           "transit_energy", "heat_flux", "max_velocity_at", "min_altitude_for"]

G0 = 9.81           # m/s2
V_ESCAPE = 11186.0  # m/s, Earth escape velocity at the surface


def _range_ok(distance_m: float, g: float = 1.0, *_, **__) -> "str | None":
    if distance_m <= 0 or g <= 0:
        return "distance and acceleration must be > 0"
    v = math.sqrt(g * G0 * distance_m)
    if v > V_ESCAPE:
        return (f"peak velocity {v/1000:.1f} km/s exceeds Earth escape velocity "
                f"({V_ESCAPE/1000:.1f} km/s) at {g:g} g; beyond "
                f"{max_range(g)/1000:.0f} km this profile is a departure, not a hop, "
                f"and the coast phase it needs is not modelled")
    return None


@formula(number=28, name="Transit time", expression="t = 2*sqrt(d/a),  a = g*9.81",
         units="s (d in m, g in units of standard gravity)",
         status=Status.DER, source="D-713",
         domain=_range_ok,
         domain_text="peak velocity must stay below Earth escape velocity: "
                     "d <= 12,786 km at 1 g, d <= 1,421 km at 9 g")
def transit_time(distance_m: float, g: float = 1.0) -> float:
    """Continuous accelerate-then-decelerate transit time.

    >>> round(transit_time(930e3, g=1.0) / 60, 1)      # London-Berlin at 1 g
    10.3
    >>> round(transit_time(930e3, g=9.0) / 60, 1)      # the same at 9 g
    3.4
    """
    return 2.0 * math.sqrt(distance_m / (g * G0))


@formula(name="Peak velocity", expression="v = sqrt(a*d)", units="m/s",
         status=Status.DER, source="D-713", domain=_range_ok,
         domain_text="same escape-velocity ceiling as the transit-time law")
def peak_velocity(distance_m: float, g: float = 1.0) -> float:
    """Velocity at the midpoint of the profile.

    >>> round(peak_velocity(930e3, g=1.0) / 1000, 1)
    3.0
    """
    return math.sqrt(g * G0 * distance_m)


@formula(name="Maximum range of the transit law",
         expression="d_max = v_escape^2 / a", units="m",
         status=Status.DER, source="D-713",
         domain=lambda g: "g must be > 0" if g <= 0 else None,
         domain_text="g > 0")
def max_range(g: float = 1.0) -> float:
    """Distance beyond which the transit-time law stops being valid.

    Lower acceleration gives **more** reach, which is counter-intuitive and correct:
    ``v = sqrt(a*d)``.

    >>> round(max_range(1.0) / 1000)
    12755
    >>> round(max_range(9.0) / 1000)
    1417
    """
    return V_ESCAPE ** 2 / (g * G0)


@formula(number=32, name="Transit energy", expression="E = m*a*d  (accelerate + brake)",
         units="J", status=Status.DER, source="D-715",
         domain=lambda mass_kg, distance_m, g=1.0, efficiency=1.0: (
             "mass and distance must be > 0" if min(mass_kg, distance_m) <= 0 else
             "efficiency must lie in (0, 1]" if not 0 < efficiency <= 1 else None),
         domain_text="mass, distance > 0; 0 < efficiency <= 1")
def transit_energy(mass_kg: float, distance_m: float, g: float = 1.0,
                   efficiency: float = 1.0) -> float:
    """Energy for the full profile, with no recovery in braking.

    **Linear in the acceleration.** Dropping from 9 g to 1 g divides the energy by 9
    and multiplies the time by 3 — and the time does not matter, because the act is
    97 % paperwork.

    >>> round(transit_energy(1000, 930e3, g=1.0) / 3.6e6)      # kWh
    2534
    >>> round(transit_energy(1000, 930e3, g=9.0) / 3.6e6)
    22808
    """
    return mass_kg * (g * G0) * distance_m / efficiency


# ── heating ───────────────────────────────────────────────────────────────────
_K_SG = 1.83e-4          # Sutton-Graves constant, SI
_SIGMA = 5.670374419e-8  # Stefan-Boltzmann


@formula(name="Stagnation heat flux (Sutton-Graves)",
         expression="q = K*sqrt(rho/R)*v^3,  K = 1.83e-4 SI",
         units="W/m2", status=Status.LIT, source="Sutton & Graves 1971",
         domain=lambda density, velocity, nose_radius_m=1.5: (
             "density, velocity and nose radius must be > 0"
             if min(density, velocity, nose_radius_m) <= 0 else None),
         domain_text="all arguments > 0")
def heat_flux(density: float, velocity: float, nose_radius_m: float = 1.5) -> float:
    """Convective heating at the stagnation point."""
    return _K_SG * math.sqrt(density / nose_radius_m) * velocity ** 3


@formula(name="Radiative-equilibrium velocity ceiling",
         expression="v_max = ( eps*sigma*T^4 / (K*sqrt(rho/R)) )^(1/3)",
         units="m/s", status=Status.DER, source="D-717",
         domain=lambda density, t_max_k=723.0, emissivity=0.8, nose_radius_m=1.5: (
             "density must be > 0" if density <= 0 else
             "temperature must be > 0 K" if t_max_k <= 0 else
             "emissivity must lie in (0, 1]" if not 0 < emissivity <= 1 else None),
         domain_text="density > 0; T > 0; 0 < emissivity <= 1. "
                     "Default T = 723 K is the creep threshold of steel, NOT a "
                     "thermal-expansion budget")
def max_velocity_at(density: float, t_max_k: float = 723.0,
                    emissivity: float = 0.8, nose_radius_m: float = 1.5) -> float:
    """Fastest the shell may go at a given air density and still keep its form.

    The criterion is **permanent deformation, not temperature difference**: thermal
    expansion is reversible and the destination floor is established after cooling, so
    what matters is creep. For steel that is ~450 C.

    >>> round(max_velocity_at(1.225) / 1000, 2)        # sea level
    0.42
    >>> round(max_velocity_at(8.0e-6) / 1000, 2)       # ~85 km
    3.08
    """
    q_max = emissivity * _SIGMA * t_max_k ** 4
    return (q_max / (_K_SG * math.sqrt(density / nose_radius_m))) ** (1.0 / 3.0)


# US Standard Atmosphere, coarse table; enough to answer "how high must I be?"
_ATM = [(0, 1.225), (20e3, 8.9e-2), (50e3, 1.03e-3), (70e3, 8.3e-5),
        (85e3, 8.0e-6), (100e3, 5.6e-7), (115e3, 1.4e-7), (150e3, 1.2e-8)]


@formula(name="Minimum altitude for a given velocity",
         expression="lowest tabulated altitude where q(rho, v) <= q_max",
         units="m", status=Status.DER, source="D-717",
         domain=lambda velocity, **kw: "velocity must be > 0" if velocity <= 0 else None,
         domain_text="velocity > 0; altitude resolved on a coarse standard-atmosphere table")
def min_altitude_for(velocity: float, **kw) -> float:
    """Altitude above which this speed does not cook the shell.

    **Velocity and density can never both be high.** This is the max-Q management any
    launch vehicle already does; the framework simply had not looked at it for 715
    decisions.

    >>> round(min_altitude_for(peak_velocity(930e3, g=1.0)) / 1000)
    85
    """
    for alt, rho in _ATM:
        if velocity <= max_velocity_at(rho, **kw):
            return float(alt)
    raise ValueError(f"no tabulated altitude admits {velocity/1000:.1f} km/s")
