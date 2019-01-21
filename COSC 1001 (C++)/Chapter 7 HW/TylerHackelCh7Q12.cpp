#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

void getScores(string[], int, double[]);
void calculateAverage(double scores[], int size, double averages[], char letterGrades[]);

int main(){
	
	//Variables
	const int classSize = 5,
			  numberOfTests = 4;
	string studentNames[classSize];
	char letterGrades[classSize];
	double score1[numberOfTests],
		   score2[numberOfTests],
		   score3[numberOfTests],
		   score4[numberOfTests],
		   score5[numberOfTests],
		   averages[classSize];
	
	//Get student names
	for(int i=0; i<classSize; i++){
		cout << "Enter student " << i+1 << "'s "
			 << "name: ";
		cin >> studentNames[i];
	}
	cout << endl;
	
	//Get test scores
	getScores(studentNames, numberOfTests, score1);
	getScores(studentNames, numberOfTests, score2);
	getScores(studentNames, numberOfTests, score3);
	getScores(studentNames, numberOfTests, score4);
	getScores(studentNames, numberOfTests, score5);
	
	//Calculate average scores and letter grades
	calculateAverage(score1, numberOfTests, averages, letterGrades);
	calculateAverage(score2, numberOfTests, averages, letterGrades);
	calculateAverage(score3, numberOfTests, averages, letterGrades);
	calculateAverage(score4, numberOfTests, averages, letterGrades);
	calculateAverage(score5, numberOfTests, averages, letterGrades);
	
	//display results
	for(int i=0; i<classSize; i++){
		cout << fixed << setprecision(2) << studentNames[i] << " recieves an average of " << averages[i] << "%" << endl;
		cout << "Their letter grade is: " << letterGrades[i] << endl << endl;
	}
	
	
	return 0;
}

void calculateAverage(double scores[], int size, double averages[], char letterGrades[]){
	static int count = 0;
	double total = 0;
	double average = 0;
	for(int i = 0; i < size; i ++){
		total += scores[i];
	}
	average	= total / size;
	averages[count] = average;
	if(average >= 90){
	    letterGrades[count] = 'A';
	}
	else if(average >= 80){
	    letterGrades[count] = 'B';
	}
	else if(average >= 70){
	    letterGrades[count] = 'C';
	}
	else if(average >= 60){
	    letterGrades[count] = 'D';
	}
	else{
		letterGrades[count] = 'F';
	}
	
	count++;
	
	return;
}

void getScores(string names[], int size, double scores[]){
	static int count = 0;
	cout << "Enter test scores for " << names[count] << endl;
	count++;
	for(int i=0; i<size; i++){
		cout << "Test " << i+1 << ": ";
		cin >> scores[i];
		while(scores[i] < 0 || scores[i] > 100){
			cout << "Invalid entry!\n";
			cout << "Enter score between 0 - 100: ";
			cin >> scores[i];
		}
	}
	cout << endl;

	return;
}

/**
Question 46
	No, the code will not print the correct sum of values for both arrays.
	Mistake one: The for loop needs to count from "<=24"
	Mistake two: Total needs to be reinitialized to 0 before totaling numberArray2.

Question 82
	int table[10];
	for(int x = 0; x < 10; x++){
		cout << "Enter the next value: ";
		cin >> table[x];
	}


*/