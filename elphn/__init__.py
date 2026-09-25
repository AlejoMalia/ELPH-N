# -*- coding: utf-8 -*-
"""ELPH-N — metrological certification of the continuous custody of a closed volume.

A reference implementation of the framework's published formulas, in which **every
formula carries its own evidentiary status, units and domain of validity, and refuses
to be used outside the range its authors verified**.

    >>> import elphn
    >>> v = elphn.contract_holds(om_impostor=4.993e-2, om_act=8.16e-4)
    >>> bool(v)
    True
    >>> elphn.transit_time(930e3, g=1.0) / 60          # doctest: +ELLIPSIS
    10.2...

Calling a formula outside its domain raises rather than returning a plausible number:

    >>> elphn.transit_time(5570e3, g=9.0)              # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    elphn.evidence.DomainError: Transit time: peak velocity ... exceeds Earth escape...

**No figure in this package comes from a bench measurement.** Every value is a
derivation, a simulation or a citation, and ``elphn.formulary()`` prints which is which.
The framework stands at 87.5 % across eight axes of completeness; the eighth axis,
MEASURED, stands at 0 %.
"""
from .evidence import (Status, DomainError, FormulaInfo, formula, registry,  # noqa: F401
                       formulary)
from .contract import (disagreement, band, dead_zone, contract_holds, far_bound,  # noqa: F401
                       decidability, materiality, Verdict)
from .kinematics import (G0, V_ESCAPE, transit_time, peak_velocity, max_range,  # noqa: F401
                         transit_energy, heat_flux, max_velocity_at, min_altitude_for)
from .instrument import (structure_exponent, gate0, pct_inv, dynamic_threshold,  # noqa: F401
                         floor_noise, Gate0Result)
from .limbo import Limbo, limbo_risk, elasticity, total_exposure  # noqa: F401
from .scale import (bubble_ceiling, seats_for, wall_thickness, shell_mass,  # noqa: F401
                    energy_per_person)

__version__ = "0.1.0"
__author__ = "Alejo Malia"
__license__ = "CC BY-NC-SA 4.0"

FRAMEWORK_COMPLETENESS = 0.875   # 8 axes; the eighth (MEASURED) is at 0.0
BENCH_VALIDATION = 0.0
REFUTATION_COST_EUR = 25         # GATE-0 with a ring plate. See experiments/GATE0_placa_A4.pdf
