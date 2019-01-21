#include <iostream>
#include <string>
using namespace std;

struct Example{
	int hours;
	double pay;
	double grossPay;
};

int main(){
	
	int cents = 698;
	int dollars = 0;
	dollars = cents / 100;
	cout << cents % 100 << " Cents" << endl;
	cout << "$" << dollars;
	/*
	int size = 50;
	unsigned long int first = 0,
					  second = 1,
					  third;
	unsigned long int fibonaccoi2[size] = {first, second};	
	
	for(int i = 2; i < size; i++){
		fibonaccoi2[i] = fibonaccoi2[i-2] + fibonaccoi2[i-1];	
		
	}

	for(int i = size - 1; i>= 0; i--){
		cout << fibonaccoi2[i] << endl;
	}	
	**/
	
	return 0; 
}



