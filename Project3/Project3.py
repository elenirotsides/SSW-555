"""
Names: Dave Taveras, Eleni Rotsides, Joshua Hector, Julio Lora
Pledge: I pledge my honor that I have abided by the Stevens Honor System
Date: Feb 21st, 2022
Assignment: Project 3
Professor: Ens
Course: SSW 555 Agile Methods

Note: This program uses tabulate to print a user friendly table
please install with:
	pip3 install tabulate
"""

from datetime import datetime
from tabulate import tabulate

individuals = {}
families = {}

months = {
	"JAN":"01",
	"FEB":"02",
	"MAR":"03",
	"APR":"04",
	"MAY":"05",
	"JUN":"06",
	"JUL":"07",
	"AUG":"08",
	"SEP":"09",
	"OCT":"10",
	"NOV":"11",
	"DEC":"12",
}

def birth_before_death(birthDate, deathDate):
    # User Story 03: Birth should occur before death of an individual
    if deathDate == "NA" or birthDate == "NA":
        return "NA"
    return birthDate < deathDate

def eval():
	try:
		file = open("Project 01.ged", 'r')
	except:
		print("Could not open file!")
		exit()
		
	now = datetime.now()
	year = int(now.strftime("%Y"))
	
	#reading lines 
	lines = file.readlines()
	id_ = ""
	fid = ""
	alive = True
	flag = ""
	for line in lines:
		#store the level, tag, and arg
		tokens = line.split()
		level = tokens[0]
		tag = tokens[1]
		args = tokens[2:]
		
		for i in range(len(args)):
			if args[i] == "INDI":
				#If new individual is being defined create new dict entry
				id_ = tag
				tag = args[i]
				args[i] = id_

				if individuals.get(id_) == None:
					individuals[id_] = {"Alive": True, "Death":"NA"}
			elif args[i] == "FAM":
				fid = tag
				tag = args[i]
				args[i] = fid 

				if families.get(fid) == None:
					families[fid] = {"Children":[], "Married": "NA", "Divorced": "NA", "Husband ID": "NA", "Wife ID": "NA", "Wife Name": "NA", "Husband Name": "NA"}

		#check tags 
		if tag == "DEAT":
			alive = False
			flag = "DEAT"
			individuals[id_]["Alive"] = False

		if tag == "BIRT" or tag == "MARR" or tag == "DIV":
			flag = tag

		if tag == "DATE":
			date = args[2] + "-" + months[args[1]] + "-" +  args[0]
			if flag == "DEAT":
				individuals[id_]["Death"] = date
				flag = ""
			if flag == "BIRT":
				age = year - int(args[2])
				individuals[id_]["Age"] = age
				individuals[id_]["Birthday"] = date
				flag = ""
			if flag == "MARR":
				families[fid]["Married"] = date
				flag = ""
			if flag == "DIV":
				families[fid]["Divorced"] = date
				flag = ""

		if tag == "NAME": 
			individuals[id_]["Name"] = args[0] + " " + args[1]
   
		if tag == "SEX":
			individuals[id_]["Gender"] = args[0]
   
		if tag == "FAMC":
			individuals[id_]["Child"] =  "{" + args[0] + "}"
			individuals[id_]["Spouse"] = "NA"
   
		if tag == "FAMS":
			individuals[id_]["Spouse"] = "{'" + args[0] + "'}"
			individuals[id_]["Child"] = "NA"
   
		if tag == "HUSB":
			families[fid]["Husband ID"] = args[0]
			families[fid]["Husband Name"] = individuals[args[0]]["Name"]
   
		if tag == "WIFE":
			families[fid]["Wife ID"] = args[0]
			families[fid]["Wife Name"] = individuals[args[0]]["Name"]
   
		if tag == "CHIL":
			families[fid]["Children"] += args


	individuals_table = []
	ind_headers = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
	for ind,value in individuals.items():
		individuals_table += [[ind, value["Name"], value["Gender"], value["Birthday"], value["Age"], value["Alive"], value["Death"], value["Child"], value["Spouse"]]]

	family_table = []
	family_headers = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
	
	for fam, value in families.items():
		family_table += [[fam, value["Married"], value["Divorced"], value["Husband ID"], value["Husband Name"], value["Wife ID"], value["Wife Name"], value["Children"]]]
		
	print("Individuals")
	print(tabulate(individuals_table, ind_headers, tablefmt="pretty"))
	print("Families")
	print(tabulate(family_table, family_headers, tablefmt="pretty"))

	file.close()
	return

if __name__ == "__main__":
    eval()