"""
Names: Dave Taveras, Eleni Rotsides, Joshua Hector, Julio Lora
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Assignment: GEDCOM Project
Course: SSW 555
Professor: Ens
"""

from datetime import datetime

#dict to store month values for comparisons
months = {
				"JAN":1,
				"Jan":1,
				"FEB":2,
				"Feb":2,
				"MAR":3,
				"Mar":3,
				"APR":4,
				"Apr":4,
				"MAY":5,
				"May":5,
				"JUN":6,
				"Jun":6,
				"JUL":7,
				"Jul":7,
				"AUG":8,
				"Aug":8,
				"SEP":9,
				"Sep":9,
				"OCT":10,
				"Oct":10,
				"NOV":11,
				"Nov":11,
				"DEC":12,
				"Dec":12
				}

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

	#get current date in (DD MMM YYYY) format
	now = datetime.now()
	year = now.strftime("%Y")
	month = now.strftime("%b")
	day = now.strftime("%d")

	#split date into tokens for analysis
	tokens = date.split()

	#Compare the Year
	if tokens[2] < year:
		return True
	if tokens[2] == year:
		#Compare the Month if years are equal
		if months[tokens[1]] < months[month]:
			return True
		if months[tokens[1]] == months[month]:
			#Compare the day if months are equal
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

    # assuming birth_date and marriage_date are both given in the correct format...
    if marriage_date == "NA" or birth_date == "NA":
        return "NA"
    return birth_date < marriage_date



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
		#if m_date was provided, then there is an issue with main code
		raise ValueError("Error: Marriage date provided should not be NA.")

	if(d_date == "NA"):
		#if person has not died then any marriage date is valid
		return True


	#Creating marriage date from substrings of m_date
	m_tokens = m_date.split("-")

	#Creating death date from substrings of d_date
	d_tokens = d_date.split("-")

	if m_tokens[0] < d_tokens[0]:
		return True
	if m_tokens[0] == d_tokens[0]:
		#If years are equal check months
		if m_tokens[1] < d_tokens[1]:
			return True
		if m_tokens[1] == d_tokens[1]:
			#If months are equal check days
			if m_tokens[2] <= d_tokens[2]:
				#Check days
				return True

	return False



"""
****************************************************************
User Story 06: Divorce Before Death
Author: Julio Lora
"""
def is_divorce_before_death(divorce_date, death_date_husb, death_date_wife,):
    if death_date_husb == "NA" or death_date_wife == "NA":
        if not death_date_husb == "NA":
            return divorce_date < death_date_husb
        if not death_date_wife == "NA":
            return divorce_date < death_date_wife
        return True
    if divorce_date == "NA":
        return "NA"
    if divorce_date < death_date_husb and divorce_date < death_date_wife:
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