# -*- coding: utf-8 -*-
"""Evidentiary bookkeeping — the part of ELPH-N that is worth stealing.

Every published formula in this package is wrapped by :func:`formula`, which attaches
to it four things the framework refuses to let a number travel without:

``status``   where the number comes from: MEAS_ADJ, MEAS_PRO, DER, LIT or DEC.
``units``    so that a dimensionally invalid threshold cannot hide behind a fitted
             exponent, which is how ``C <= 12 um`` survived 1,800 fields without
             ever biting (decision D-669).
``domain``   a predicate over the arguments. Outside it the call **raises**, because
             the transit-time law silently returns beautiful numbers well past the
             point where its own profile exceeds Earth escape velocity (D-713).
``source``   the decision or citation that established it.

The design claim is narrow and testable: *a scientific library should refuse to be
used outside the domain its authors verified.* Most do not, and the failure is
silent. Here it is loud.
"""
from __future__ import annotations

import functools
import inspect
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

__all__ = ["Status", "DomainError", "formula", "registry", "formulary", "FormulaInfo"]


class Status:
    """Evidentiary status. The weights are the ones used to combine independent lines."""

    MEAS_ADJ = "MEAS_ADJ"   # measured against a traceable standard
    MEAS_PRO = "MEAS_PRO"   # measured on our own bench, no traceability
    DER = "DER"             # derived from measured or cited quantities
    LIT = "LIT"             # taken from the literature
    DEC = "DEC"             # declared: a modelling choice, not a finding

    WEIGHT = {MEAS_ADJ: 0.95, MEAS_PRO: 0.85, DER: 0.70, LIT: 0.60, DEC: 0.30}

    @classmethod
    def doubt(cls, *statuses: str) -> float:
        """Residual doubt over INDEPENDENT lines of evidence, capped at 0.99.

        >>> round(Status.doubt(Status.DER, Status.LIT), 4)
        0.12
        """
        d = 1.0
        for s in statuses:
            d *= 1.0 - cls.WEIGHT[s]
        return min(d, 0.99)


class DomainError(ValueError):
    """Raised when a formula is called outside the domain its authors verified."""


@dataclass
class FormulaInfo:
    number: Optional[int]
    name: str
    expression: str
    units: str
    status: str
    source: str
    domain_text: str
    func: Callable[..., Any] = field(repr=False, default=None)

    def __str__(self) -> str:  # pragma: no cover - presentation only
        n = f"{self.number:>2}. " if self.number else "    "
        return (f"{n}{self.name}\n"
                f"      {self.expression}\n"
                f"      units  {self.units}\n"
                f"      status {self.status}   source {self.source}"
                + (f"\n      domain {self.domain_text}" if self.domain_text else ""))


_REGISTRY: Dict[str, FormulaInfo] = {}


def formula(*, number: Optional[int] = None, name: str, expression: str, units: str,
            status: str, source: str,
            domain: Optional[Callable[..., Optional[str]]] = None,
            domain_text: str = ""):
    """Attach evidentiary metadata to a function and enforce its domain.

    ``domain`` receives the same arguments as the function and returns ``None`` when
    the call is admissible, or a string explaining the violation, which becomes the
    :class:`DomainError` message.
    """
    if status not in Status.WEIGHT:
        raise ValueError(f"unknown status {status!r}")

    def deco(fn):
        info = FormulaInfo(number, name, expression, units, status, source,
                           domain_text, fn)
        sig = inspect.signature(fn)

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            if domain is not None:
                # Bind and apply defaults before checking: a domain predicate that
                # only saw the positional arguments would skip every default, which
                # is exactly the case a caller is most likely to use.
                bound = sig.bind(*args, **kwargs)
                bound.apply_defaults()
                why = domain(*bound.args, **bound.kwargs)
                if why:
                    raise DomainError(f"{name}: {why}  [{source}]")
            return fn(*args, **kwargs)

        wrapper.info = info
        info.func = wrapper
        _REGISTRY[f"{fn.__module__.split('.')[-1]}.{fn.__name__}"] = info
        return wrapper

    return deco


def registry() -> Dict[str, FormulaInfo]:
    """Every published formula, keyed ``module.function``."""
    return dict(_REGISTRY)


def formulary(status: Optional[str] = None) -> str:
    """The formulary as text, optionally filtered by evidentiary status."""
    import elphn  # noqa: F401  - ensure every module is imported and registered

    rows = [i for i in _REGISTRY.values() if status is None or i.status == status]
    rows.sort(key=lambda i: (i.number is None, i.number or 0, i.name))
    counts: Dict[str, int] = {}
    for i in _REGISTRY.values():
        counts[i.status] = counts.get(i.status, 0) + 1
    head = "  ·  ".join(f"{k} {v}" for k, v in sorted(counts.items()))
    return (f"ELPH-N formulary — {len(rows)} formulas\n{head}\n\n"
            + "\n\n".join(str(i) for i in rows))
