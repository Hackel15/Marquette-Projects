#include <iostream>
#include <string>
#include <iomanip>
#include <fstream>
using namespace std;

//structures
struct WeightLift{
	string legs,
		   biceps;
};
struct User{
	string name;
	WeightLift personalLifts;
};

//prototypes
void getUserNames(User& n);
void displayOptions();
void chooseOption(char& c);

int main(){
	User person;
	char choice;
	//fstream 
	if(person.name.size() < 1){
		getUserNames(person);
	}else{
		cout << "Hello " << person.name;
		cout << ".\n";
	}
	displayOptions();	
	chooseOption(choice);
	switch(choice){
		case 'A':
		
				 break;
		
		case 'B':
		
				 break;
				 
		case 'C':
				 
				 break;
		
		
		
	}
	
	return 0;
}

void getUserNames(User& n){
	cout << "Enter user: ";
	getline(cin, n.name);
	cout << endl << "Hello " << n.name;
	cout << ".\n";
	return;
}

void displayOptions(){
	cout << "Enter letter for option selection.\n";
	cout << "A) Generate complete workout\n";
	cout << "B) Choose specific lift\n";
	cout << "C) Add exercise to library\n";
	return;
}

void chooseOption(char& c){
	cout << "Enter option: ";
	cin >> c;
	c = toupper(c);
	while(!(c >= 'A' && c <= 'C')){
		cout << "Invalid!\n";
		cout << "Enter option: ";
		cin >> c;
		c = toupper(c);
	}
	return;
}






