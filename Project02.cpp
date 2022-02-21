/*********************************************
Name: Dave Taveras
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Date: February 14th, 2022
Assignment: Project 02
Course: SSW 555
Professor: Ens
*********************************************/
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>

using namespace std;

int main (int argc, char** argv){
	string line = "";
	string token = "";

	unordered_map<string, string> tag = {
		// hashtable to store the tag as the key and the level as the value.
		// using -1 for zero since entries default to 0 value
		// if they are not in the table
		{"INDI", "-1"},
		{"NAME", "1"},
		{"SEX" , "1"},
		{"BIRT", "1"},
		{"DEAT", "1"},
		{"FAMC", "1"},
		{"FAMS", "1"},
		{"FAM" , "-1"},
		{"MARR", "1"},
		{"HUSB", "1"},
		{"WIFE", "1"},
		{"CHIL", "1"},
		{"DIV" , "1"},
		{"DATE", "2"},
		{"HEAD", "-1"},
		{"TRLR", "-1"},
		{"NOTE", "-1"}
		
	};

	//open the file
	//fstream file("Project 01.ged");
	fstream file("test.ged");
	if(!file.is_open()){
		// File could not be opened 
		cout << "File could not be opened!" << endl;
		exit(0);
	}

	//get lines of file
	while(getline(file, line)){
		stringstream iss(line);
		vector<string> tokens;

		//print the line
		cout << "--> " << line << endl;

		//break line into tokens
		while(getline(iss, token, ' ')){
			for(size_t k = 0; k < token.length(); k++){
				// erase carrage characters
				if(token[k] == '\r'){
					token.erase(token.begin()+token.length()-1);
				}
			}
			// Add tokens to tokens vector
			tokens.push_back(token);
		}
		bool flag = true;
		//perform validation of inputs
		for(size_t i = 0; i < tokens.size(); i++){
			if(flag == false){
				break;
			}
			switch(i){
				case 0:
					if((tokens[0] != "0") && (tokens[0] != "1") && (tokens[0] != "2")){
						//if this is true the level is not a valid level
						flag = false;
					}
					break;
				case 1:
					if(tag[tokens[i]] == "0"){
						//if this is true the tag is not a valid tag
						flag = false;
					}else{
						// if this section is entered the tag was valid
						if(tokens[0] == "0"){
							if(tag[tokens[i]] != "-1"){
								// if this is true, a tag that is not associated with level 0 was provided
								if(tokens.size() > 2){
									if(tokens[i+1].compare("INDI")!=0 && tokens[i+1].compare("FAMS")!= 0){
										//if this is true, then line did not follow exception cases:
										//0 <id> INDI or 0 <id> FAMS
										flag = false;
									}else{
										// switch positions of the tag and argument
										string temp = tokens[i];
										tokens[i] = tokens[i+1];
										tokens[i+1] = temp;
									}
								}else{
									// if this is entered, an invalid tag was provided 
									flag = false;
								}
							}
						}
						else if(tag[tokens[i]] != tokens[0]){
							//if this is true, the tag did not match the associated level
							flag = false;
						}
					}
					break;
				default:
					break;
			}
		}

		// Print evaluation in desired format
		for(size_t i = 0; i < tokens.size(); i++){
			if(i == 0){
				cout << "<-- ";
			}
			if(i < 2){
				cout << tokens[i] << "|";
			}
			if(i == 1){
				if(flag == false){
					cout << "N|";
				}else{
					cout << "Y|";
				}
			}
			if(i >= 2){
				cout << tokens[i] << " ";
			}
		}
		cout << endl;


	}
	// close the file
	file.close();
	return 0;
}