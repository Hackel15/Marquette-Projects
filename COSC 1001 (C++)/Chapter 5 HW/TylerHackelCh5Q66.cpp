#include <iostream>
using namespace std;

int main()
{
	int num1, num2;
	char again;
	
	do{
		cout << "Enter a number: ";
		cin >> num1;
		cout << "Enter another number: ";
		cin >> num2;
		cout << "There sum is " << (num1 + num2) << endl;
		cout << "Do you want to do this again Y or N?\n";
		cin >> again;
		
	}while(again == 'y' || again == 'Y');


	return 0;
}