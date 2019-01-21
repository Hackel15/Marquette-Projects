#include <iostream>
#include <iomanip>
using namespace std;

//functions
void getJudgeData(double& score1);
void calcScore(double score1, double score2, double score3, double score4, double score5, double& average);
double findLowest(double score1, double score2, double score3, double score4, double score5);
double findHighest(double score1, double score2, double score3, double score4, double score5);
void validateScores(double validate);

int main(){
	
	//variables
	double judge1,
		   judge2,
		   judge3,
		   judge4,
		   judge5,
		   judgeAverage;
		 
	//call function to get scores
	getJudgeData(judge1);
	getJudgeData(judge2);
	getJudgeData(judge3);
	getJudgeData(judge4);
	getJudgeData(judge5);
	cout << "Score 1: " << judge1 << endl;
	cout << "Score 2: " << judge2 << endl;
	cout << "Score 3: " << judge3 << endl;
	cout << "Score 4: " << judge4 << endl;
	cout << "Score 5: " << judge5 << endl;
	//call function to get average of scores
	//eliminating the highest and lowest scores
	calcScore(judge1, judge2, judge3, judge4, judge5, judgeAverage);
	cout << fixed << setprecision(1);
	cout << "The average of the three scores is: " << judgeAverage << endl;
			
	return 0;
}

void getJudgeData(double& score1){
	static int count=1;
	cout << "Enter score number " << count << ": ";
	cin >> score1;
	while(!(score1 >= 0 && score1 <= 10)){
		cout << "Scores entered must be between 0 points - 10 points.\n";
		cout << "Enter score: ";
		cin >> score1;
	}
	count++;	
	return;
}

void calcScore(double score1, double score2, double score3, double score4, double score5, double& average){
	
	double lowestScore = findLowest(score1, score2, score3, score4, score5);
	double highestScore = findHighest(score1, score2, score3, score4, score5);
	//cout << "Verify lowest score in calcScore function: " << lowestScore << endl;
	//cout << "Verify highest score in calcScore function: " << highestScore << endl;
	average = (score1 + score2 + score3 + score4 + score5 - lowestScore - highestScore) / 3;
	cout << fixed << setprecision(1);
	//cout << "Verify average in calcScore function: " << average << endl;
	return;
}

double findLowest(double score1, double score2, double score3, double score4, double score5){
	double lowest;
	if(score1 <= score2 && score1 <= score3 && score1 <= score4 && score1 <= score5){
		lowest = score1;
		//cout << "The lowest outlier in findLowest function is: " << lowest << endl;
		return lowest;
	}
	else if(score2 <= score1 && score2 <= score3 && score2 <= score4 && score2 <= score5){
		lowest = score2;
		//cout << "The lowest outlier in findLowest function is: " << lowest << endl;
		return lowest;
	}
	else if(score3 <= score2 && score3 <= score1 && score3 <= score4 && score3 <= score5){
		lowest = score3;
		//cout << "The lowest outlier in findLowest function is: " << lowest << endl;
		return lowest;
	}
	else if(score4 <= score2 && score4 <= score3 && score4 <= score1 && score1 <= score5){
		lowest = score4;
		//cout << "The lowest outlier in findLowest function is: " << lowest << endl;
		return lowest;
	}
	else{
		lowest = score5;
		//cout << "The lowest outlier in findLowest function is: " << lowest << endl;
		return lowest;
	}
}

double findHighest(double score1, double score2, double score3, double score4, double score5){
	double highest;
	if(score1 >= score2 && score1 >= score3 && score1 >= score4 && score1 >= score5){
		highest = score1;
		//cout << "The highest outlier in findHighest function is: " << highest << endl;
		return highest;
	}
	else if(score2 >= score1 && score2 >= score3 && score2 >= score4 && score2 >= score5){
		highest = score2;
		//cout << "The highest outlier in findHighest function is: " << highest << endl;
		return highest;
	}
	else if(score3 >= score1 && score3 >= score2 && score3 >= score4 && score3 >= score5){
		highest = score3;
		//cout << "The highest outlier in findHighest function is: " << highest << endl;
		return highest;
	}
	else if(score4 >= score1 && score4 >= score2 && score4 >= score3 && score4 >= score5){
		highest = score4;
		//cout << "The highest outlier in findHighest function is: " << highest << endl;
		return highest;
	}
	else{
		highest = score5;
		//cout << "The highest outlier in findHighest function is: " << highest << endl;
		return highest;
	}
}

void validateScores(double validate){
	
	cout << "Enter score: ";
	cin >> validate;
	while(!(validate >= 0 || validate <= 10)){
		cout << "Scores entered must be between 0 points - 10 points.\n";
		cout << "Enter score: ";
		cin >> validate;
	}
	
	return;
}

/**
//Q59

void getValue(int& value){
	cout << "Enter a value: ";
	cin >> value;
}
*/