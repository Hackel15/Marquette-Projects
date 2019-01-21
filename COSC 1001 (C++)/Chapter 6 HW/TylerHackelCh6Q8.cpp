//Question #8
#include <iostream>
#include <ctime>
#include <stdlib.h>
using namespace std;

void coinToss();

int main()
{
	int numberOfFlips;
	cout << "This program simulates the tossing of a coin\n";
	cout << "Enter the amount of time you'd like to flip the coin: ";
	cin >> numberOfFlips;
	unsigned seed = time(0);
	srand(seed);
	for(int count = 1; count <= numberOfFlips; count++){
		cout << "Flip " << count << " = ";
		coinToss();
	}	
	return 0;
}

void coinToss(){
	int coin = rand() % 2 + 1;
	if(coin == 1){
		cout << "heads" << endl;
	}
	else if(coin == 2){
		cout << "tails" << endl;
	}
	return;
}





/**
//#32

showValue(2);

//#56

int total(int value1, int value2, int value3){
	
	return value1 + value2 + value3;
}
*/