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
# Dict to store months with 31 days
thirty_one = {
    "01": 0,
    "03": 0,
    "05": 0,
    "07": 0,
    "08": 0,
    "10": 0,
    "12": 0,
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
User Story 04: Marriage Before Divorce
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
User Story 07: Less than 150 years old
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
User Story 13: Siblings Spacing
Author: Dave Taveras
"""


def siblingsSpacing(id_, fid, ind_dict, fam_dict):
    """
        This function checks to see if the birth of siblings
        in a family is at 1 day or 9 months apart
        @returns True if properly spaced
        @returns False if not
    """
    # get the individual's bday tokens as integers
    bday_tokens = list(map(int, ind_dict[id_]["Birthday"].split("-")))
    twins = False
    for sibling in fam_dict[fid]["Children"]:
        twins = False
        # get the sibling's bday tokens as integers
        sib_bday_tokens = list(
            map(int, ind_dict[sibling]["Birthday"].split("-")))
        # Check if individual has a twin born 1 day apart or same day
        if bday_tokens[0] == sib_bday_tokens[0] and bday_tokens[1] == sib_bday_tokens[1] and abs(bday_tokens[2] - sib_bday_tokens[2]) <= 1:
            twins = True
        # Use earlier date for calculations
        # If true current individual's birthday comes before sibling's
        if compareDates(ind_dict[id_]["Birthday"], ind_dict[sibling]["Birthday"]) == True:

            # finding next closest date that sibling can be born
            # if current month + 9 is greater than 12 roll into next year and compare
            if bday_tokens[1] + 9 > 12:
                bday_tokens[1] = (bday_tokens[1]+9) % 12
                bday_tokens[0] = bday_tokens[0] + 1
                if compareDates((str(bday_tokens[0])+"-"+"{:02}".format(bday_tokens[1])+"-"+"{:02}".format(bday_tokens[2])), ind_dict[sibling]["Birthday"]) == False:
                    if twins == False:
                        return False
            # if current month + 9 is not greater than 12, add months and compare
            else:
                bday_tokens[1] = bday_tokens[1] + 9
                if compareDates((str(bday_tokens[0])+"-"+"{:02}".format(bday_tokens[1])+"-"+"{:02}".format(bday_tokens[2])), ind_dict[sibling]["Birthday"]) == False:
                    if twins == False:
                        return False
        # if current sibling's birthday comes before indivudual's
        else:
            # finding next closest date that sibling can be born
            # if current month + 9 is greater than 12 roll into next year and compare
            if sib_bday_tokens[1] + 9 > 12:
                sib_bday_tokens[1] = (sib_bday_tokens[1]+9) % 12
                sib_bday_tokens[0] = sib_bday_tokens[0] + 1
                if compareDates((str(sib_bday_tokens[0])+"-"+"{:02}".format(sib_bday_tokens[1])+"-"+"{:02}".format(sib_bday_tokens[2])), ind_dict[id_]["Birthday"]) == False:
                    if twins == False:
                        return False
            # if current month + 9 is not greater than 12, add months and compare
            else:
                sib_bday_tokens[1] = sib_bday_tokens[1] + 9
                if compareDates((str(sib_bday_tokens[0])+"-"+"{:02}".format(sib_bday_tokens[1])+"-"+"{:02}".format(sib_bday_tokens[2])), ind_dict[id_]["Birthday"]) == False:
                    if twins == False:
                        return False

    # all siblings were properly spaced apart
    return True


"""
****************************************************************
User Story 14: Multiple births <= 5
Author: Eleni Rotsides
"""


def no_more_than_5_births(individual_dict, families_dict):
    """No more than five siblings should be born at the same time. Returns an error for every family where this rule is being violated."""
    errors_to_be_printed = ''
    for famID, family in families_dict.items():
        birthdays = {}
        if len(family["Children"]) >= 5:
            for child in family["Children"]:
                if birthdays.get(individual_dict[child]["Birthday"]) == None:
                    birthdays[individual_dict[child]["Birthday"]] = 1
                else:
                    birthdays[individual_dict[child]["Birthday"]] += 1
        for i, num_birthdays in birthdays.items():
            if num_birthdays >= 5:
                errors_to_be_printed += f"Error: FAMILY: US14: {famID}: No more than five siblings should be born at the same time.\n"
    return errors_to_be_printed


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
User Story 20: Aunts and Uncles
Author: Julio Lora
"""


def aunts_and_uncles(husband_id, wife_id, family_dict, individual_dict):
    """
        This function checks to see if a married couple includes an aunt and nephew or uncle and niece

        returns true if it does
        returns false if not
    """

    # Initialize various variables
    husband_siblings = []
    wife_siblings = []
    husband_father_id = ""
    husband_mother_id = ""
    wife_father_id = ""
    wife_mother_id = ""

    # Get the family that the husband is in
    husband_family_id = individual_dict[husband_id]["Child"]

    if (husband_family_id != 'NA'):
        for person in family_dict[husband_family_id]["Children"]:
            # Add to list of husband_siblings
            husband_siblings.append(person)
        # Remove the husband from the list of his own siblings
        husband_siblings.remove(husband_id)
        # Get husbands father
        husband_father_id = family_dict[husband_family_id]["Husband ID"]
        # Get husbands mother
        husband_mother_id = family_dict[husband_family_id]["Wife ID"]

    # Get the family that the wife is in
    wife_family_id = individual_dict[wife_id]["Child"]

    if (wife_family_id != 'NA'):
        for person in family_dict[wife_family_id]["Children"]:
            # Add to list of wife_siblings
            wife_siblings.append(person)
        # Remove the wife from the list of her own siblings
        wife_siblings.remove(wife_id)
        # Get wifes father
        wife_father_id = family_dict[wife_family_id]["Husband ID"]
        # Get wifes mother
        wife_mother_id = family_dict[wife_family_id]["Wife ID"]

    # Check if the husband is the uncle of the wife
    if (wife_father_id in husband_siblings) or (wife_mother_id in husband_siblings):
        return True

    # Checks if the wife is the aunt of the husband
    if (husband_father_id in wife_siblings) or (husband_mother_id in wife_siblings):
        return True

    return False


"""
****************************************************************
User Story 21: Correct Gender Roles
Author: Julio Lora
"""


def correct_gender_roles(fam_dict, ind_dict):
    """
    This function searches the families dictionary to ensure that each husband is male and each wife is female

    @returns true if the husbands are male and the wifes are female / false if not

    """

    husband_ID = ""
    wife_ID = ""

    for family in fam_dict:
        husband_ID = fam_dict[family]["Husband ID"]
        wife_ID = fam_dict[family]["Wife ID"]
        if (husband_ID != 'NA' and wife_ID != 'NA'):
            if (ind_dict[husband_ID]["Gender"] != 'M'):
                return False
            if (ind_dict[wife_ID]["Gender"] != 'F'):
                return False
    return True


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
User Story 23: Unique Name and Birthday
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
User Story 25: Unique First Name in Family
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
User Story 29: List Deceased
Author: Julio Lora
"""


def list_deceased(ind_dict):
    """
    This function iterates the dictionary and returns a list of all deceased people

    @returns list of deceased people

    """
    deceased_list = []
    for person in ind_dict:
        if (ind_dict[person]["Death"] != 'NA'):
            deceased_list.append(ind_dict[person]["Name"])
    return deceased_list


"""
****************************************************************
User Story 30: List Living Married
Author: Julio Lora
"""


def list_living_married(ind_dict):
    """
    This function iterates the dictionary and returns a list of all people who are living and married

    @returns list of people who are living and married

    """
    living_married_list = []
    for person in ind_dict:
        if (ind_dict[person]["Spouse"] != 'NA'):
            if (ind_dict[person]["Death"] == 'NA'):
                living_married_list.append(ind_dict[person]["Name"])

    return living_married_list


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


"""
****************************************************************
User Story 33: Orphaned Children
Author: Joshua Hector
"""


def orphaned_children(families_dict, individuals_dict):
    """List all orphaned children (both parents dead and child < 18 years old) 
    in a GEDCOM file."""

    orphan_list = []

    for family in families_dict.values():
        if len(family["Children"]) != 0:
            for individual in individuals_dict.values():
                if family["Husband Name"] == individual["Name"]:
                    husband = individual

                if family["Wife Name"] == individual["Name"]:
                    wife = individual

            if husband["Death"] != "NA" and wife["Death"] != "NA":
                for child in family["Children"]:
                    for individual in individuals_dict.values():
                        if child == individual["ID"]:
                            child_indi = individual
                            if int(child_indi["Age"]) < 18:
                                orphan_list.append(child_indi['Name'])

    if len(orphan_list) == 0:
        return False
    else:
        return orphan_list


"""
****************************************************************
User Story 34: Large Age Differences
Author: Joshua Hector
"""


def large_age_diff(families_dict, individuals_dict):
    """List all couples who were married when the older 
    spouse was more than twice as old as the younger spouse. """

    couples = []

    for family in families_dict.values():
        married_date = family['Married'].split("-")[0]
        for individual in individuals_dict.values():
            if family["Husband ID"] == individual["ID"]:
                husband = individual
                husband_birth_date = husband["Birthday"].split("-")[0]
            if family["Wife ID"] == individual["ID"]:
                wife = individual
                wife_birth_date = wife["Birthday"].split("-")[0]

        husband_age_when_married = int(married_date) - int(husband_birth_date)
        wife_age_when_married = int(married_date) - int(wife_birth_date)

        if (husband_age_when_married / wife_age_when_married) > 2 or (wife_age_when_married / husband_age_when_married) > 2:
            couples.append(husband["Name"])
            couples.append(wife["Name"])

    if len(couples) == 0:
        return False
    else:
        return couples


"""
****************************************************************
User Story 42: Reject Illegitimate Dates
Author: Dave Taveras
"""


def rejectIllegitimateDates(date):
    """
    This function checks to see if a provided date is
    legitimate or not
    @returns false if not legitimate
    @returns true if legitimate

    """
    d_tokens = date.split("-")
    is_leap = False
    # check for incorrect month or day number
    if int(d_tokens[1]) > 12 or int(d_tokens[2]) > 31:
        return False
    # check if year divides by 4 for leap year
    if int(d_tokens[0]) % 4 == 0:
        is_leap = True
    # if this is None then month has only 30 days or is February
    if thirty_one.get(d_tokens[1]) == None:
        # if month provided is february and year is not a leap year
        if int(d_tokens[1]) == 2 and is_leap == False:
            # 28 days for non leap year
            if int(d_tokens[2]) <= 28:
                return True
        # if month provided is february and is a leap year
        elif int(d_tokens[1]) == 2 and is_leap == True:
            # 29 days for leap year
            if int(d_tokens[2]) <= 29:
                return True
        # if month provided is not February then it must have 30 days
        elif int(d_tokens[1]) != 2:
            if int(d_tokens[2]) <= 30:
                return True
    # if not None then month provided has 31 days and cannot be February
    else:
        if int(d_tokens[2]) <= 31:
            return True
    # if checks are not met, date was illegitimate
    return False
