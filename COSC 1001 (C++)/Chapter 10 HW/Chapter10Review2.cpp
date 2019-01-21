//Review for Exam #4

#include <iostream>
#include <string>
using namespace std;

int main(){
	
	/**
	string title = "System Engineer";
	cout << title << endl;
	cout << title.substr(title.find('e'), 5) << endl;
	*/
	
	string foo = "alpha";
	string bar = "beta";
	
	/**
		what is the difference between these two statements:
		cin >> name;
		getline(cin, name);
	*/
	
	/**
		first, ask the user to enter one whole line of string, and store
		it in variable line of string type.
		ssecondly, count how many ',' are in the line, and how many '!'
		are in the line. Then output the total number.
	*/
	int total = 0;
	string name;
	cout << "Enter string: ";
	getline(cin, name);
	for(int i = 0; i < name.length(); i++){
		if(name[i] == ',' || name[i] == '!'){
			total++;
		}
	}
	cout << "The total is: " << total << endl;
	
	
	
	return 0;
}









