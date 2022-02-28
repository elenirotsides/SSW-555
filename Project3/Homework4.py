"""
Unit tests for Project3.py

@author: Joshua Hector
"""

import unittest
from Project3 import birth_before_death
import datetime


class TestBirthBeforeDeath(unittest.TestCase):
    def test_no_death(self):
        """Returns NA if individual is not dead"""
        self.assertEqual(birth_before_death(
            datetime.date(1999, 8, 27), "NA"), "NA")
        
    def test_no_birth(self):
        """Returns NA if individual is not dead"""
        self.assertEqual(birth_before_death(
            "NA", datetime.date(1999, 8, 27)), "NA")

    def test_birth_before_death(self):
        """Returns True if birth before death"""
        self.assertTrue(birth_before_death(
            datetime.date(1999, 12, 11), datetime.date(2078, 6, 11)), True)
        
    def test_birth_before_death2(self):
        """Returns True if birth before death"""
        self.assertTrue(birth_before_death(
            datetime.date(2020, 12, 11), datetime.date(2020, 12, 12)), True)

    def test_death_before_birth(self):
        """Returns False if birth after death"""
        self.assertFalse(birth_before_death(
            datetime.date(1999, 12, 11), datetime.date(1995, 6, 11)), False)

if __name__ == '__main__':
    unittest.main()