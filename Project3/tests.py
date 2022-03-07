"""
Unit tests for Project3.py

@author: Eleni Rotsides, Julio Lora
"""

import unittest
from Project3 import is_birth_before_marriage, is_divorce_before_death, birth_before_death, parents_not_too_old
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

#The following lists and objects are intended to be used for the parents_not_too_old tests since it takes a list of children as input
Dan = {
    "Name": "Dan",
    "Age": 14
    }
Maria = {
    "Name": "Maria",
    "Age": 20
    }
John = {
    "Name": "Maria",
    "Age": 5
    }
Julia = {
    "Name": "Maria",
    "Age": 25
    }
motherChildren = [Dan, Maria, John]
fatherChildren = [John, Julia]

class TestParentsNotTooOld(unittest.TestCase):
    def test_mother_too_old(self):
        """Returns False if mother is over 60 years older than the children"""
        self.assertEqual(parents_not_too_old(motherChildren, fatherChildren, 80, 45), False)
    def test_mother_not_too_old(self):
        """Returns True if mother is not over 60 years older than the children"""
        self.assertEqual(parents_not_too_old(motherChildren, fatherChildren, 50, 45), True)
    def test_father_too_old(self):
        """Returns False if father is over 80 years older than the children"""
        self.assertEqual(parents_not_too_old(motherChildren, fatherChildren, 45, 90), False)
    def test_father_not_too_old(self):
        """Returns True if father is not over 80 years older than the children"""
        self.assertEqual(parents_not_too_old(motherChildren, fatherChildren, 50, 45), True)
        


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
