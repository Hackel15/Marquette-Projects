#include <iostream>
using namespace std;

int main()
{
	int userNumber;
	int sum;
	int count;
	
	sum = 0;
	cout << "Enter 10 numbers: \n";
	for(count = 1; count <= 10; count++){
		cout << "Enter number " << count << ": ";
		cin >> userNumber;
		sum += userNumber;
	}
	cout << "The sum of your 10 numbers is " << sum;
	
	return 0;
}