#include <iostream>
using namespace std;

int main()
{
	int numberOne;
	int numberTwo;
	int sum;   
	char userChoice;
	
	do{
		cout << "Enter two number: ";
		cin >> numberOne >> numberTwo;
		sum = numberOne + numberTwo;
		cout << "The sum of " << numberOne << " + " << numberTwo << " = " << sum;
		cout << endl << "Do you wish to preform the operation again?\n";
		cout << "Enter Y to continue or N to end program: ";
		cin >> userChoice;
	}while(userChoice == 'y' || userChoice == 'Y');

	return 0;
}