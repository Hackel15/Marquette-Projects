#include <iostream>
#include <string>
using namespace std;

struct Earnings{
	int firstQuarter,
		secondQuarter,
		thirdQuarter,
		fourthQuarter,
		totalRevenue;	
};

struct MovieData{
	string title[],
		   director[],
		   yearReleased[],
		   runningTime[];
	Earnings sales;
};

void getMovieInfo(MovieData& m, int s);
void displayMovies(MovieData m, int s);

int main(){
	enum Time {2000, 2001, 2003};
	Time year;
	MovieData warrenTheater[];
	
	
	for(int i = 0; i<movieCount; i++){
		getMovieInfo(warrenTheater[i], movieCount);
	}
	cout << "\tMOVIES\n";
	for(int i = 0; i<movieCount; i++){
		displayMovies(warrenTheater[i], movieCount);
	}
	
	return 0;
}

void getMovieInfo(MovieData& m, int s){
		int n;
		cout << "How many movies were played in year?\n";
		cin >> n;
		for(int i = 0; i<n; i++){
		cout << "Enter movie title " << i << ":";
		getline(cin, m.title[i]);
		cout << "Enter movie director " << i << ":";
		getline(cin, m.director[i]);
		cout << "Enter year released " << i << ":";
		getline(cin, m.yearReleased[i]);
		cout << "Enter movie legnth " << i << ":";
		getline(cin, m.runningTime[i]);		
		}
	return;
}

void displayMovies(MovieData m, int s){
	cout << m.title << endl;
	cout << m.director << endl;
	cout << m.yearReleased << endl;
	cout << m.runningTime << " minutes." << endl;
	cout << endl;
	
	return;
}
