#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

void futureValue(double presentValue, double monthlyInterest, int months, double& futureBalance);

int main()
{
	//variables
	int monthsHeld;
	double accountInterest,
		   endBalance,
		   accountBalance;
		   
	// Get User Information	   
	cout << "Enter account balance: ";
	cin >> accountBalance;
	cout << "Enter account interest: ";
	cin >> accountInterest;
	cout << "Enter number of months held: ";
	cin >> monthsHeld;
	
	//call compound monthly interest equation
	futureValue(accountBalance, accountInterest, monthsHeld, endBalance);
	
	//display future value
	cout << "After " << monthsHeld << " months at a " << fixed << setprecision(2) << accountInterest << " percent interest\n";
	cout << "your account balance will be $" << endBalance << endl;
	
	
	return 0;
}

void futureValue(double presentValue, double monthlyInterest, int months, double& futureBalance){
	
	//monthlyInterest += 1;
	futureBalance = presentValue * pow(1 + monthlyInterest, months);
		
	return;
}

/**
//Q34

result = cube(4);

//Q36

display(age, income, initial);

*/