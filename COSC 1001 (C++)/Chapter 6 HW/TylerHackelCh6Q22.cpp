#include <iostream>
using namespace std;

bool isPrime(int primeNumber);

int main(){
	
	//variables
	int userNumber;
	bool result;
	
	//User enters a number
	cout << "This program determines whether a number is prime.\n";
	cout << "Enter a number of your choice: ";
	cin >> userNumber;
	cout << endl;
	
	//call function & return results
	result = isPrime(userNumber);
	if(result == false){
		cout << "The number " << userNumber << " is NOT";
		cout << " a prime number.\n";
	}
	else{
		cout << "The number " << userNumber << " is a";
		cout << " prime number.\n";
	}
	
	return 0;
}

bool isPrime(int primeNumber){
	bool result;
	for(int count = 2; count < primeNumber; count++){
		if(primeNumber % count == 0){
			result = false;
			return result;
		}
	}
	result = true;
	return result;
}