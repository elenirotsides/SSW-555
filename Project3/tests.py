"""
Unit tests for Project3.py

@author: Eleni Rotsides
"""

import unittest
from Project3 import is_birth_before_marriage
import datetime


class TestBirthBeforeMarriage(unittest.TestCase):
    def test_no_marriage(self):
        """Returns NA if marriage doesn't exist"""
        self.assertEqual(is_birth_before_marriage(
            datetime.date(1999, 8, 27), "NA"), "NA")

    def test_no_birth_date(self):
        """Returns NA if birth date doesn't exist"""
        self.assertEqual(is_birth_before_marriage(
            "NA", datetime.date(1999, 8, 27)), "NA")

    def test_birth_is_before_marriage(self):
        """Returns true if birth is before marriage"""
        self.assertEqual(is_birth_before_marriage(datetime.datetime(
            1990, 3, 15), datetime.datetime(2020, 1, 1)), True)

    def test_birth_is_not_before_marriage(self):
        """Returns false if birth is not before marriage"""
        self.assertAlmostEqual(is_birth_before_marriage(datetime.datetime(2020, 1, 1), datetime.datetime(
            1990, 3, 15)), False)

    def test_nothing_is_given(self):
        """Returns NA if both arguments are NA"""
        self.assertEqual(is_birth_before_marriage("NA", "NA"), "NA")


if __name__ == '__main__':
    unittest.main()
