#include <iostream>
using namespace std;

int main()
{
	int enterMonth;
	int enterYear;
	int leapYear;
	
	
	cout << "Enter a month (1 - 12): ";
	cin >> enterMonth;
	cout << "Enter a year: ";
	cin >> enterYear;
	
	if(enterYear % 100 == 0 && enterYear % 400 == 0){
		leapYear = 29;
	}
	else if(enterYear % 100 != 0 && enterYear % 4 == 0){
		leapYear = 29;
	}
	else{
		leapYear = 28;
	}
	
	if(enterMonth >= 1 && enterMonth <= 12){
		
		switch(enterMonth){
		
			case 1:
				cout << "31 days";
				break;
			
			case 2:
				cout << leapYear << " days";
				break;
			
			case 3:
				cout << "31 days";
				break;
			
			case 4:
				cout << "30 days";
				break;
			
			case 5:
				cout << "31 days";
				break;
			
			case 6:
				cout << "30 days";
				break;
			
			case 7:
				cout << "31 days";
				break;
			
			case 8:
				cout << "31 days";
				break;
			
			case 9:
				cout << "30 days";
				break;
			
			case 10:
				cout << "31 days";
				break;
			
			case 11:
				cout << "30 days";
				break;
			
			case 12:
				cout << "31 days";
				break;
		}
	}
	
	else{
		cout << "Invalid month!";
	}

	return 0;
}