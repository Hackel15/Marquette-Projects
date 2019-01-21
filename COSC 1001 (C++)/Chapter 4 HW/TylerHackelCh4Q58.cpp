// This program averages 3 test scores.
// It uses the variable perfectScore as a flag.
#include <iostream>
using namespace std;

int main()
{
	bool perfectScore;
	double average;
	int score1, score2, score3;
		
	cout << "Enter your 3 test scores and I will average them: ";
	cin >> score1 >> score2 >> score3;
	average = (score1 + score2 + score3) / 3.0; 
	
	if(average == 100){
		perfectScore = true;
		
		if(perfectScore){
			cout << "Congratulations!\n";
			cout << "That's a perfect score.\n";
			cout << "You deserved a pat on the back!\n";
		}
	}
	else{
		cout << "Your average is " << average << endl;
	}
	
	return 0;
}


	
/**
	Question 32
	
	if(y == 10){
		
		x = 0;
	}
	else{
		
		x = 1;
	}
*/
