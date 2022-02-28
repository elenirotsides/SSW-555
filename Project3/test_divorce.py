"""
Unit tests for Project3.py

@author: Julio Lora
"""

import unittest
from Project3 import is_divorce_before_death
import datetime


class TestBirthBeforeMarriage(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()