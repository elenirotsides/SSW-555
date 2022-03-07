"""
Unit tests for Project3.py

@author: Eleni Rotsides
"""

import unittest
from Project3 import *
from Homework4 import dateBeforeCurrent
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


class TestDivorceBeforeDeath(unittest.TestCase):
    def test_no_death(self):
        """Returns True if both spouses have not passed away"""
        self.assertEqual(is_divorce_before_death(
            datetime.date(1999, 8, 27), "NA", "NA"), True)

    def test_divorce_before(self):
        """Returns True if the divorce happened before the death of both spouses"""
        self.assertEqual(is_divorce_before_death(
            datetime.date(1999, 8, 27), datetime.date(2005, 8, 27), datetime.date(2010, 8, 27)), True)

    def test_husband_passed(self):
        """Returns True if the divorce happened before the death of the husband"""
        self.assertEqual(is_divorce_before_death(
            datetime.date(1999, 8, 27), datetime.date(1999, 9, 27), "NA"), True)

    def test_wife_passed(self):
        """Returns True if the divorce happened before the death of the wife"""
        self.assertEqual(is_divorce_before_death(
            datetime.date(1999, 8, 27), "NA", datetime.date(1999, 9, 27)), True)

    def test_death_before(self):
        """Returns False if the divorce happened after the death of both spouses"""
        self.assertEqual(is_divorce_before_death(
            datetime.date(1999, 8, 27), datetime.date(1999, 5, 27), datetime.date(1999, 4, 27)), False)

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

class TestMarriageBefore14(unittest.TestCase):
    def test_marriage_same_date(self):
        """Returns False if the marriage is the same date as the wife and husband birth date"""
        self.assertFalse(marriage_before_14(
            datetime.date(1999, 8, 27), datetime.date(1999, 8, 27), datetime.date(1999, 8, 27)), False)

    def test_husband_birth_before_marriage(self):
        """Returns False if the husband is married before the age of 14"""
        self.assertEqual(marriage_before_14(
            datetime.date(2008, 8, 1), datetime.date(1999, 1, 1), datetime.date(1980, 10, 27)), False)

    def test_wife_birth_before_marriage(self):
        """Returns True if the divorce happened before the death of the husband"""
        self.assertEqual(marriage_before_14(
            datetime.date(2010, 6, 11), datetime.date(1990, 5, 20), datetime.date(1997, 12, 25)), False)
        
    def test_marriage_valid(self):
        """Returns True if the divorce happened before the death of the wife"""
        self.assertEqual(marriage_before_14(
            datetime.date(2015, 2, 20), datetime.date(1980, 10, 10), datetime.date(1990, 9, 27)), True)

    def test_no_marriage(self):
        """Returns False if the divorce happened after the death of both spouses"""
        self.assertEqual(marriage_before_14(
            "NA", datetime.date(1999, 5, 27), datetime.date(1999, 4, 27)), "NA")

        
class TestHomework4(unittest.TestCase):
    # User story 1: Dates before Current Date
    def test_dateBeforeCurrent1(self):
        result = dateBeforeCurrent("31 AUG 2000")
        self.assertTrue(result)

    def test_dateBeforeCurrent2(self):
        result = dateBeforeCurrent("9 DEC 2025")
        self.assertFalse(result)

    def test_dateBeforeCurrent3(self):
        result = dateBeforeCurrent("28 FEB 1990")
        self.assertTrue(result)

    def test_dateBeforeCurrent4(self):
        result = dateBeforeCurrent("21 FEB 2022")
        self.assertEqual(result, True)

    def test_dateBeforeCurrent5(self):
        result = dateBeforeCurrent("11 MAR 2022")
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
