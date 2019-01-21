#include <iostream>
using namespace std;

int main()
{
	int numCount, count, num;
	double average, total;
	
	total = 0;
	cout << "How many numbers do you want to average? ";
	cin >> numCount;
	for(count = 1; count <= numCount; count++){
		cout << "Enter number " << count << ": ";
		cin >> num;
		total += num;
	}
	average = (total / numCount);
	cout << "The average of the " << numCount << " numbers entered is: ";
	cout << average;
	
	return 0;
}