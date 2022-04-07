"""
Names: Dave Taveras, Eleni Rotsides, Joshua Hector, Julio Lora
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Assignment: GEDCOM Project
Course: SSW 555
Professor: Ens
"""

from datetime import datetime

# dict to store month values for comparisons
months = {
    "JAN": 1,
    "Jan": 1,
    "FEB": 2,
    "Feb": 2,
    "MAR": 3,
    "Mar": 3,
    "APR": 4,
    "Apr": 4,
    "MAY": 5,
    "May": 5,
    "JUN": 6,
    "Jun": 6,
    "JUL": 7,
    "Jul": 7,
    "AUG": 8,
    "Aug": 8,
    "SEP": 9,
    "Sep": 9,
    "OCT": 10,
    "Oct": 10,
    "NOV": 11,
    "Nov": 11,
    "DEC": 12,
    "Dec": 12
}


def compareDates(date1, date2):
    # helper function to check if date 1 comes before date 2
    # Dates provided must be in YYYY-MM-DD format

    # create tokens from date 1
    d1_tokens = date1.split("-")

    # Create tokens from date 2
    d2_tokens = date2.split("-")

    if d1_tokens[0] < d2_tokens[0]:
        return True
    if d1_tokens[0] == d2_tokens[0]:
        # If years are equal check months
        if d1_tokens[1] < d2_tokens[1]:
            return True
        if d1_tokens[1] == d2_tokens[1]:
            # If months are equal check days
            if d1_tokens[2] <= d2_tokens[2]:
                # Check days
                return True
    return False


"""
****************************************************************
User Story 01: datesBeforeCurrent
Author: Dave Taveras
"""


def dateBeforeCurrent(date):
    """
            this boolean function is to be called to validate a date.
            this only ensures a date does not come from the future.
            returns true if date comes from past or current date
            returns false if date comes from future.
            date should be in the format:
            Day, Month, Year
    """

    # get current date in (DD MMM YYYY) format
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%b")
    day = now.strftime("%d")

    # split date into tokens for analysis
    tokens = date.split()

    # Compare the Year
    if tokens[2] < year:
        return True
    if tokens[2] == year:
        # Compare the Month if years are equal
        if months[tokens[1]] < months[month]:
            return True
        if months[tokens[1]] == months[month]:
            # Compare the day if months are equal
            if tokens[0] <= day:
                return True

    return False


"""
****************************************************************
User Story 02: Birth Before Marriage
Author: Eleni Rotsides
"""


def is_birth_before_marriage(birth_date, marriage_date):
    """Returns True if birth is before marriage, False if it isn't, and NA if marriage doesn't exist"""

    # Dates should be in the format "YYYY-MM-DD"

    # Creating birth date from substrings of birth_date
    b_tokens = birth_date.split("-")

    # Creating marriage date from substrings of marriage_date
    m_tokens = marriage_date.split("-")

    # assuming birth_date and marriage_date are both given in the correct format...
    if marriage_date == "NA" or birth_date == "NA":
        return "NA"
    return b_tokens[0] < m_tokens[0]


"""
****************************************************************
User Story 03: Birth Before Death
Author: Joshua Hector
"""


def birth_before_death(birthDate, deathDate):
    # User Story 03: Birth should occur before death of an individual
    if deathDate == "NA" or birthDate == "NA":
        return "NA"
    return birthDate < deathDate


"""
****************************************************************
User Story 4: Marriage Before Divorce
Author: Dave Taveras
"""


def marriageBeforeDivorce(marriageDate, divorceDate):
    return compareDates(marriageDate, divorceDate)


"""
****************************************************************
User Story 05: Marriage Before Death
Author: Dave Taveras
"""


def marriageBeforeDeath(m_date, d_date):
    """
    Checks if date of marriage occurs before
    date of death. Both dates are in the format:
    "YYYY-MM-DD"

    note: m_date should not be "NA" since function should
    be called if a marriage date is provided
    """
    if(m_date == "NA"):
        # if m_date was provided, then there is an issue with main code
        raise ValueError("Error: Marriage date provided should not be NA.")

    if(d_date == "NA"):
        # if person has not died then any marriage date is valid
        return True

    return compareDates(m_date, d_date)


"""
****************************************************************
User Story 06: Divorce Before Death
Author: Julio Lora
"""


def is_divorce_before_death(divorce_date, death_date_husb, death_date_wife,):
    if(divorce_date == "NA"):
        raise ValueError("Error: Divorce date provided should not be NA.")

    if death_date_husb == "NA" or death_date_wife == "NA":
        if not death_date_husb == "NA":
            return compareDates(divorce_date, death_date_husb)
        if not death_date_wife == "NA":
            return compareDates(divorce_date, death_date_wife)
        return True
    if compareDates(divorce_date, death_date_husb) and compareDates(divorce_date, death_date_wife):
        return True
    return False


"""
****************************************************************
User Story 10: Marriage Before Age of 14
Author: Joshua Hector
"""


def marriage_before_14(marriage_date, birth_date_husb, birth_date_wife):
    """Returns true if the marriage date is before the age of 14 for BOTH husband and wife"""
    if marriage_date == "NA":
        return "NA"
    # if the marriage date is before the birth dates of both the husband and wife, return False
    if marriage_date < birth_date_husb or marriage_date < birth_date_wife:
        return False

    # have the year of the birth dates allocated to named variables
    marriage_year = marriage_date.year
    birth_year_husb = birth_date_husb.year
    birth_year_wife = birth_date_wife.year

    # checks to see that the marriage is after the birthdate of the husband and wife all at the same time
    if marriage_date > birth_date_husb and marriage_date > birth_date_wife:
        return (marriage_year - birth_year_wife > 14) & (marriage_year - birth_year_husb > 14)


"""
****************************************************************
User Story 12: Parents are not too old
Author: Julio Lora
"""


def parents_not_too_old(motherChildren, fatherChildren, mother_age, father_age):
    for child in motherChildren:
        if (mother_age - child["Age"]) > 60:
            return False
    for child in fatherChildren:
        if (father_age - child["Age"]) > 80:
            return False
    return True


"""
****************************************************************
User Story 7: Less than 150 years old
Author: Eleni Rotsides
"""


def is_less_than_150(birth, current, death):
    """Death should be less than 150 years after birth for dead people, and
    current date should be less than 150 years after birth for all living people
    returns boolean"""

    # Expects given dates to be in the format "YYYY-MM-DD"

    # Creating birth date from substrings of birth
    b_tokens = birth.split("-")

    # Creating current date from substrings of current
    c_tokens = current.split("-")

    # Creating death date from substrings of death
    d_tokens = death.split("-")

    if death != "NA" and birth != "NA":
        return int(d_tokens[0]) < (150 + int(b_tokens[0]))
    elif current != "NA":
        return int(c_tokens[0]) < (150 + int(b_tokens[0]))
    else:
        return "Not enough information supplied"


"""
****************************************************************
User Story 16: Male last names
Author: Eleni Rotsides
"""


def male_same_last_name(individuals_dict, families_dict, familyID):
    """All male members of a family should have the same last name"""

    family = families_dict.get(familyID)
    husband_last_name = ""

    if family["Husband Name"] != "NA":
        husband_last_name = family["Husband Name"].split()[1]

        if family["Children"] != []:
            children = family["Children"]

            for child in children:
                individual = individuals_dict.get(child)
                child_last_name = individual["Name"].split()[1]

                if individual["Gender"] == "M" and (child_last_name != husband_last_name):
                    raise ValueError(
                        "Error: FAMILY: US16: All male members of " + familyID + " do not have the same last name.")
            return True
    else:
        raise ValueError(
            "Error: FAMILY: US16: No husband in family " + familyID + ".")


"""
****************************************************************
User Story 15: Fewer than 15 siblings
Author: Joshua Hector
"""


def fewer_than_15_siblings(families_dict, family_id):
    """Returns true if the amount of siblings in a family is less than 15."""
    # family_list = []
    family = families_dict.get(family_id)

    # for fam in family["Children"]:
    #     if len(fam) >= 15:
    #         family_list.append(fam)

    if len(family["Children"]) > 15:
        return False
    else:
        return True


"""
****************************************************************
User Story 17: No marriages to descendants
Author: Joshua Hector
"""


def no_marriage_to_descendants(families_dict):
    """Returns True if there are no parents that are married to their descendants."""
    wrong_parent_marry = []

    for fam, value in families_dict.items():
        if (families_dict[fam]["Wife ID"] in families_dict[fam]["Children"]) or (families_dict[fam]["Husband ID"] in families_dict[fam]["Children"]):
            wrong_parent_marry.append(fam)

    if len(wrong_parent_marry) > 0:
        return False
    else:
        return True


"""
****************************************************************
User Story 18: Siblings should not marry
Author: Eleni Rotsides
"""


def is_siblings_married(individuals_dict, families_dict):
    """Checks every entry in families_dict and individuals_dict and ensures that
    marriage is not between siblings. Raises ValueError if siblings are married and
    returns False if all marriages are good."""

    for index, family in families_dict.items():
        if family["Children"] != []:
            children = family["Children"]

            for child in children:
                individual = individuals_dict.get(child)

                for ind, family in families_dict.items():
                    if individual["Spouse"] == ("{'"+ind+"'}"):
                        raise ValueError(
                            "Error: FAMILY: US18: Siblings should not be married.")
    return False


"""
****************************************************************
User Story 31: List living single
Author: Eleni Rotsides
"""


def list_living_single(individuals_dict, families_dict):
    """Returns a list of all living people over 30 who have never been married in a GEDCOM file"""

    single_people = []  # will contain a list of individuals that have never been married
    for i, person in individuals_dict.items():
        # A flag that will will be used to mark a person as never having been married while also being above 30 years of age
        person["Single"] = False

        if person["Spouse"] == "NA" and person["Age"] > 30:
            # check to see if they've been married before; if not, add to single_people list
            for j, family in families_dict.items():
                if family["Husband ID"] == i or family["Wife ID"] == i and (family["Married"] == "NA" and family["Divorced"] == "NA" and not person["Single"]):
                    if family["Husband ID"] == "NA" or family["Wife ID"] == "NA":
                        single_people.append(person)
                        person["Single"] = True

            # at this point, person isn't in families table, but spouse field is marked as NA, so they haven't been married, so add to list
            # after checking that they haven't been flaged as single
            if not person["Single"]:
                single_people.append(person)
                person["Single"] = True

    listOfSingletons = ""
    for person in single_people:
        listOfSingletons += f'{person["Name"]} is over the age of 30 and has never been married.\n'

    return listOfSingletons


"""
****************************************************************
User Story 22: All ID's Are Unique
Author: Dave Taveras
"""


def uniqueIds(id_, ind_dict):
    """
    This function iterates a dictionary to ensure that the
    given id is not already present

    @returns true if unique / false if not
    """
    for key in ind_dict:
        if id_ == key:
            return False
    return True


"""
****************************************************************
User Story 23: uniqueNameAndBirthday
Author: Dave Taveras
"""


def uniqueNameAndBirthday(name, bday, ind_dict):
    """
    This function iterates the dictionary to ensure that
    the name and birthday of the individual with the given id
    is unique.

    @returns true if unique / false if not

    """

    for key, value in ind_dict.items():
        if value["Name"] == name and value["Birthday"] == bday:
            return False
    return True


"""
****************************************************************
User Story 25: uniqueFirstNameInFamily
Author: Dave Taveras
"""


def uniqueFirstNameInFamily(id_, fid, ind_dict, fam_dict):
    """
    This function searches the individuals dictionary with the id's
    provided from the familiies dictionary to ensure that each first name
    and birthday is unique in that family.

    @returns true if unique / false if not

    """

    name = ind_dict[id_]["Name"].split()[0]
    bday = ind_dict[id_]["Birthday"]

    for child in fam_dict[fid]["Children"]:
        if name == ind_dict[child]["Name"].split()[0] and bday == ind_dict[child]["Birthday"]:
            return False
    return True


"""
****************************************************************
User Story 32: List multiple births
Author: Eleni Rotsides
"""


def list_multiple_births(individuals_dict):
    """Returns a list containing all people that share a birthday"""
    multiples = {}

    # Creates a dictionary with birthdates as keys and people sharing the birthdays as values
    for i, person in individuals_dict.items():
        if person["Birthday"] in multiples:
            multiples[person["Birthday"]] += [person]
        else:
            multiples[person["Birthday"]] = [person]

    multiples_final = {}

    # adds entries of multiples to multiples_final only if there is more than 1 person born that day
    for i, people in multiples.items():
        if len(people) > 1:
            multiples_final[i] = people

    listOfMultipleBirths = ""
    for i, people in multiples_final.items():
        listOfMultipleBirths += f'On {person["Birthday"]}, the following people share a birthday: '
        for person in people:
            listOfMultipleBirths += f'{person["Name"]} '
    return listOfMultipleBirths
