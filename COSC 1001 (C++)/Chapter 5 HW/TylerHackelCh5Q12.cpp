#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	double fahrenheit;
	int celsius;
	
	cout << "This program shows the values of celsius 0 - 20\n";
	cout << "and the equivalent degrees of fahrenheit.\n";
	cout << "Press enter to see values: ";
	cin.get();
	
	for(celsius = 0; celsius <= 20; celsius++){
	    
		fahrenheit = (celsius*1.8) + 32;
		cout << fixed << setprecision(1);
		if(celsius < 10){
		    cout << "Celsius: " << celsius;
		    cout << "   =    " << "Fahrenheit: " << fahrenheit << endl;
		}
		else{
		    cout << "Celsius: " << celsius;
		    cout << "  =    " << "Fahrenheit: " << fahrenheit << endl;  
		}
	}
	
	return 0;
}