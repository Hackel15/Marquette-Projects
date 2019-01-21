#include <iostream>
using namespace std;

int main(){
	
	//Variables
	int wrongAnswers = 0,
		correctAnswers = 20,
		passingGrade = 15;
	const int size = 20;
	char answerSheet[size]={'A', 'D', 'B', 'B', 'C', 'B', 'A', 'B', 'C', 'D',
					    'A', 'C', 'D', 'B', 'D', 'C', 'C', 'A', 'D', 'B'};
	char userAnswers[size];
	
	//User enters answers
	cout << "Enter answers for driver's license exam(A,B,C,D)\n" << endl;
	for(int i=0; i < size; i++){
		cout << "Question " << (i+1) << ": ";
		cin >> userAnswers[i];
		while(!(userAnswers[i] == 'A') && !(userAnswers[i] == 'B') &&
			  !(userAnswers[i] == 'C') && !(userAnswers[i] == 'D')){
				   cout << "Invalid entry\n";
				   cout << "Enter value of A, B, C, or D: ";
				   cin >> userAnswers[i];
			   }	
	}
	
	//Calculate wrong answers
	for(int i=0; i<size; i++){
		if(answerSheet[i] != userAnswers[i]){
			wrongAnswers++;
		}
	}
	correctAnswers -= wrongAnswers;
	
	//Decide if user passes or fails
	if(correctAnswers >= passingGrade){
		cout << "You PASSED your driver's license exam!!\n"
			 << "Careful while you drive home.\n";
		cout << "Number of questions answered correctly: " << correctAnswers << endl
			 << "Number of questions anwered incorrectly: " << wrongAnswers << endl
			 << "Questions you answered wrong:\n"
			 << "Question #'s: ";
		for(int i=0; i<size; i++){
			if(answerSheet[i] != userAnswers[i]){
				cout << i + 1 << " ";
			}
		}	
	}
	else{
		cout << "You FAILED your driver's license exam..\n"
			 << "Better luck next time..";
		cout << "Number of questions answered correctly: " << correctAnswers << endl
			 << "Number of questions anwered incorrectly: " << wrongAnswers << endl
			 << "Questions you answered wrong:\n"
			 << "Question #'s: ";
		for(int i=0; i<size; i++){
			if(answerSheet[i] != userAnswers[i]){
				cout << i + 1 << " ";
			}
		}			 
	}
	
	return 0;
}