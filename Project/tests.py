"""
Names: Dave Taveras, Eleni Rotsides, Joshua Hector, Julio Lora
Pledge: I pledge my honor that I have abided by the Stevens Honor System
Assignment: GEDCOM Project
Professor: Ens
Course: SSW 555 Agile Methods
"""

import unittest
import userStories
import datetime

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


"""
****************************************************************
User Story 01: datesBeforeCurrent
Author: Dave Taveras
"""
class test_dateBeforeCurrent(unittest.TestCase):
    # User story 1: Dates before Current Date
    def test_dateBeforeCurrent1(self):
        result = userStories.dateBeforeCurrent("31 AUG 2000")
        self.assertTrue(result)

    def test_dateBeforeCurrent2(self):
        result = userStories.dateBeforeCurrent("9 DEC 2025")
        self.assertFalse(result)

    def test_dateBeforeCurrent3(self):
        result = userStories.dateBeforeCurrent("28 FEB 1990")
        self.assertTrue(result)

    def test_dateBeforeCurrent4(self):
        result = userStories.dateBeforeCurrent("21 FEB 2022")
        self.assertEqual(result, True)

    def test_dateBeforeCurrent5(self):
        result = userStories.dateBeforeCurrent("11 MAR 2022")
        self.assertEqual(result, False)



"""
****************************************************************
User Story 02: Birth Before Marriage
Author: Eleni Rotsides
"""
class test_birthBeforeMarriage(unittest.TestCase):
    def test_no_marriage(self):
        """Returns NA if marriage doesn't exist"""
        self.assertEqual(userStories.is_birth_before_marriage(
            datetime.date(1999, 8, 27), "NA"), "NA")

    def test_no_birth_date(self):
        """Returns NA if birth date doesn't exist"""
        self.assertEqual(userStories.is_birth_before_marriage(
            "NA", datetime.date(1999, 8, 27)), "NA")

    def test_birth_is_before_marriage(self):
        """Returns true if birth is before marriage"""
        self.assertEqual(userStories.is_birth_before_marriage(datetime.datetime(
            1990, 3, 15), datetime.datetime(2020, 1, 1)), True)

    def test_birth_is_not_before_marriage(self):
        """Returns false if birth is not before marriage"""
        self.assertAlmostEqual(userStories.is_birth_before_marriage(datetime.datetime(2020, 1, 1), datetime.datetime(
            1990, 3, 15)), False)

    def test_nothing_is_given(self):
        """Returns NA if both arguments are NA"""
        self.assertEqual(userStories.is_birth_before_marriage("NA", "NA"), "NA")



"""
****************************************************************
User Story 03: Birth Before Death
Author: Joshua Hector
"""
class test_birthBeforeDeath(unittest.TestCase):
    def test_no_death(self):
        """Returns NA if individual is not dead"""
        self.assertEqual(userStories.birth_before_death(
            datetime.date(1999, 8, 27), "NA"), "NA")

    def test_no_birth(self):
        """Returns NA if individual is not dead"""
        self.assertEqual(userStories.birth_before_death(
            "NA", datetime.date(1999, 8, 27)), "NA")

    def test_birth_before_death(self):
        """Returns True if birth before death"""
        self.assertTrue(userStories.birth_before_death(
            datetime.date(1999, 12, 11), datetime.date(2078, 6, 11)), True)

    def test_birth_before_death2(self):
        """Returns True if birth before death"""
        self.assertTrue(userStories.birth_before_death(
            datetime.date(2020, 12, 11), datetime.date(2020, 12, 12)), True)

    def test_death_before_birth(self):
        """Returns False if birth after death"""
        self.assertFalse(userStories.birth_before_death(
            datetime.date(1999, 12, 11), datetime.date(1995, 6, 11)), False)



"""
****************************************************************
User Story 05: Marriage Before Death
Author: Dave Taveras
"""
class test_marriageBeforeDeath(unittest.TestCase):
    def test_marriageBeforeDeath1(self):
        result = userStories.marriageBeforeDeath("2000-03-24", "2000-03-23")
        self.assertFalse(result)

    def test_marriageBeforeDeath2(self):
        result = userStories.marriageBeforeDeath("1987-05-6", "1996-09-19")
        self.assertTrue(result)

    def test_marriageBeforeDeath3(self):
        result = userStories.marriageBeforeDeath("2022-03-7", "2020-03-6")
        self.assertFalse(result)

    def test_marriageBeforeDeath4(self):
        result = userStories.marriageBeforeDeath("2005-10-25", "2005-10-26")
        self.assertEqual(result, True)

    def test_marriageBeforeDeath5(self):
        result = userStories.marriageBeforeDeath("2019-07-7", "2019-07-6")
        self.assertEqual(result, False)

    def test_marriageBeforeDeath6(self):
        self.assertRaises(ValueError, userStories.marriageBeforeDeath, "NA", "2000-03-23")

    def test_marriageBeforeDeath7(self):
        result = userStories.marriageBeforeDeath("1995-09-15", "NA")
        self.assertEqual(result, True)



"""
****************************************************************
User Story 06: Divorce Before Death
Author: Julio Lora
"""
class test_divorceBeforeDeath(unittest.TestCase):
    def test_no_death(self):
        """Returns True if both spouses have not passed away"""
        self.assertEqual(userStories.is_divorce_before_death(
            datetime.date(1999, 8, 27), "NA", "NA"), True)

    def test_divorce_before(self):
        """Returns True if the divorce happened before the death of both spouses"""
        self.assertEqual(userStories.is_divorce_before_death(
            datetime.date(1999, 8, 27), datetime.date(2005, 8, 27), datetime.date(2010, 8, 27)), True)

    def test_husband_passed(self):
        """Returns True if the divorce happened before the death of the husband"""
        self.assertEqual(userStories.is_divorce_before_death(
            datetime.date(1999, 8, 27), datetime.date(1999, 9, 27), "NA"), True)

    def test_wife_passed(self):
        """Returns True if the divorce happened before the death of the wife"""
        self.assertEqual(userStories.is_divorce_before_death(
            datetime.date(1999, 8, 27), "NA", datetime.date(1999, 9, 27)), True)

    def test_death_before(self):
        """Returns False if the divorce happened after the death of both spouses"""
        self.assertEqual(userStories.is_divorce_before_death(
            datetime.date(1999, 8, 27), datetime.date(1999, 5, 27), datetime.date(1999, 4, 27)), False)



"""
****************************************************************
User Story 10: Marriage Before Age of 14
Author: Joshua Hector
"""
class test_marriageBefore14(unittest.TestCase):
    def test_marriage_same_date(self):
        """Returns False if the marriage is the same date as the wife and husband birth date"""
        self.assertFalse(userStories.marriage_before_14(
            datetime.date(1999, 8, 27), datetime.date(1999, 8, 27), datetime.date(1999, 8, 27)), False)

    def test_husband_birth_before_marriage(self):
        """Returns False if the husband is married before the age of 14"""
        self.assertEqual(userStories.marriage_before_14(
            datetime.date(2008, 8, 1), datetime.date(1999, 1, 1), datetime.date(1980, 10, 27)), False)

    def test_wife_birth_before_marriage(self):
        """Returns True if the divorce happened before the death of the husband"""
        self.assertEqual(userStories.marriage_before_14(
            datetime.date(2010, 6, 11), datetime.date(1990, 5, 20), datetime.date(1997, 12, 25)), False)
        
    def test_marriage_valid(self):
        """Returns True if the divorce happened before the death of the wife"""
        self.assertEqual(userStories.marriage_before_14(
            datetime.date(2015, 2, 20), datetime.date(1980, 10, 10), datetime.date(1990, 9, 27)), True)

    def test_no_marriage(self):
        """Returns False if the divorce happened after the death of both spouses"""
        self.assertEqual(userStories.marriage_before_14(
            "NA", datetime.date(1999, 5, 27), datetime.date(1999, 4, 27)), "NA")



"""
****************************************************************
User Story 12: Parents are not too old
Author: Julio Lora
"""
class test_parentsNotTooOld(unittest.TestCase):
    def test_mother_too_old(self):
        """Returns False if mother is over 60 years older than the children"""
        self.assertEqual(userStories.parents_not_too_old(motherChildren, fatherChildren, 80, 45), False)
    def test_mother_not_too_old(self):
        """Returns True if mother is not over 60 years older than the children"""
        self.assertEqual(userStories.parents_not_too_old(motherChildren, fatherChildren, 50, 45), True)
    def test_father_too_old(self):
        """Returns False if father is over 80 years older than the children"""
        self.assertEqual(userStories.parents_not_too_old(motherChildren, fatherChildren, 45, 90), False)
    def test_father_not_too_old(self):
        """Returns True if father is not over 80 years older than the children"""
        self.assertEqual(userStories.parents_not_too_old(motherChildren, fatherChildren, 50, 45), True)


if __name__ == '__main__':
    unittest.main()
