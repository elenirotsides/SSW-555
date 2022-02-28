"""
Name: Dave Taveras
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Date: February 21st, 2022
Assignment: Homework 4
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
