# -*- coding: utf-8 -*-
"""Tests for the ELPH-N reference implementation.

Two kinds of test, and the second is the point of the package: that published
figures are reproduced, and that **every domain limit actually raises**. A library
whose guard rails are documented but not enforced has no guard rails.
"""
import doctest
import math
import unittest

import elphn
from elphn.evidence import DomainError, Status


class PublishedFigures(unittest.TestCase):
    """Every number the paper states must come back out of the code."""

    def test_contract_of_the_measured_act(self):
        v = elphn.contract_holds(om_impostor=4.993e-2, om_act=8.16e-4)
        self.assertAlmostEqual(v.band, 7.82, places=2)
        self.assertTrue(v.holds)

    def test_a_band_just_above_one_is_a_tie(self):
        self.assertFalse(elphn.contract_holds(1.10e-3, 1.0e-3).holds)

    def test_far_bound_reports_with_its_k(self):
        self.assertAlmostEqual(elphn.far_bound(3_000_000), 1e-6)
        self.assertAlmostEqual(elphn.far_bound(37), 0.0811, places=4)

    def test_act_is_9713_times_more_material(self):
        self.assertEqual(round(1 / elphn.materiality(3.0, 0.597, 7.80)), 9713)

    def test_london_berlin_at_1g(self):
        self.assertAlmostEqual(elphn.transit_time(930e3, g=1.0) / 60, 10.3, places=1)
        self.assertAlmostEqual(elphn.peak_velocity(930e3, g=1.0) / 1000, 3.0, places=1)
        self.assertEqual(elphn.min_altitude_for(elphn.peak_velocity(930e3)) / 1000, 85)

    def test_energy_is_linear_in_acceleration(self):
        e1 = elphn.transit_energy(1000, 930e3, g=1.0)
        e9 = elphn.transit_energy(1000, 930e3, g=9.0)
        self.assertAlmostEqual(e9 / e1, 9.0, places=9)

    def test_bubble_ceiling_and_seats(self):
        self.assertAlmostEqual(elphn.bubble_ceiling(), 5.03, places=2)
        self.assertEqual(elphn.seats_for(elphn.bubble_ceiling()), 4)

    def test_no_economy_of_scale(self):
        per1 = elphn.energy_per_person(1, 930e3)
        per6 = elphn.energy_per_person(6, 930e3)
        self.assertAlmostEqual(per1, per6, places=6)

    def test_shortest_limbo_can_be_the_most_dangerous(self):
        transit = elphn.Limbo("transit", 3.4, 0.01, p_mitigation=0.0)
        sealed = elphn.Limbo("sealed leg", 34.0, 0.01, p_mitigation=0.9)
        self.assertAlmostEqual(transit.risk, sealed.risk, places=9)
        self.assertFalse(transit.mitigated)

    def test_percentile_is_tied_to_n(self):
        self.assertAlmostEqual(elphn.pct_inv(50), 99.0, places=1)
        self.assertLess(elphn.pct_inv(10), elphn.pct_inv(50))


class DomainsAreEnforced(unittest.TestCase):
    """Each of these silently returned a plausible number before it raised."""

    def test_transit_law_refuses_beyond_escape_velocity(self):
        elphn.transit_time(1_000e3, g=9.0)                      # inside
        with self.assertRaises(DomainError) as cm:
            elphn.transit_time(5_570e3, g=9.0)                  # London-New York
        self.assertIn("escape velocity", str(cm.exception))

    def test_lower_acceleration_gives_more_reach(self):
        self.assertGreater(elphn.max_range(1.0), elphn.max_range(9.0))
        elphn.transit_time(5_570e3, g=1.0)                      # legal at 1 g

    def test_rule_of_three_refuses_nonzero_acceptances(self):
        with self.assertRaises(DomainError):
            elphn.far_bound(1000, acceptances=1)

    def test_seats_refuse_beyond_the_ceiling(self):
        with self.assertRaises(DomainError):
            elphn.seats_for(13.9)                               # the 100-seat bubble

    def test_correlation_outside_minus_one_to_one(self):
        with self.assertRaises(DomainError):
            elphn.disagreement(1.5)

    def test_limbo_rejects_impossible_probabilities(self):
        with self.assertRaises(ValueError):
            elphn.Limbo("bad", 1.0, p_event=1.5)

    def test_defaults_are_checked_too(self):
        """The domain predicate must see applied defaults, not only what was passed."""
        with self.assertRaises(DomainError):
            elphn.transit_time(20_000e3)                        # g defaults to 1.0


class Metadata(unittest.TestCase):
    """The evidentiary bookkeeping is part of the public interface."""

    def test_every_formula_declares_its_status(self):
        for key, info in elphn.registry().items():
            self.assertIn(info.status, Status.WEIGHT, key)
            self.assertTrue(info.units, key)
            self.assertTrue(info.source, key)

    def test_nothing_claims_to_be_measured_against_a_standard(self):
        """Bench validation is at 0 %: no formula may claim traceability."""
        traceable = [k for k, i in elphn.registry().items()
                     if i.status == Status.MEAS_ADJ]
        self.assertEqual(traceable, [], f"unearned traceability: {traceable}")

    def test_doubt_combines_independent_lines(self):
        self.assertAlmostEqual(Status.doubt(Status.DER, Status.LIT), 0.12, places=4)

    def test_formulary_renders(self):
        self.assertIn("ELPH-N formulary", elphn.formulary())


def load_tests(loader, tests, ignore):
    for mod in (elphn, elphn.evidence, elphn.contract, elphn.kinematics,
                elphn.instrument, elphn.limbo, elphn.scale):
        tests.addTests(doctest.DocTestSuite(mod))
    return tests


if __name__ == "__main__":
    unittest.main(verbosity=2)
