#include <iostream>
#include <string>
using namespace std;

int main(){
	int numberOfStudents;
	string name;
	string previousName;
	string firstName;
	string lastName;
	int count;
	
	cout << "Input the number of students: ";
	cin >> numberOfStudents;
	while(numberOfStudents < 1 || numberOfStudents > 25){
		cout << "Must enter a value between 1 - 25.\n";
		cout << "Input the number of students: ";
		cin >> numberOfStudents;
	}
	
	cout << "Enter name of student: ";
	cin >> name;
	firstName = name;
	lastName = name;
	previousName = name;
	
	
	for(count = 2; count <= numberOfStudents; count++){
		cout << "Enter name of student: ";
		cin >> name;
		if(name > previousName){
			if(name > lastName){
				lastName = name;
			}
		}
		else if(name < previousName){
			if(name < firstName){
				firstName = name;
			}
		}
		previousName = name;	
	}
	
	cout << "The first name is: " << firstName << endl;
	cout << "The last name is: " << lastName << endl;
	
	return 0;
}