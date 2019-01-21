#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int softwareQuantity;
	double softwareCost;
	double softwareDiscount;
	
	cout << "This software company would like to sell a\n";
	cout << "package that retails for $99.  Quantity discounts\n";
	cout << "are given acording to the following table.\n" << endl;
	
	cout << "Quantity" << setw(20) << "Discount\n" << endl;
	cout << "10-19" << setw(20) << "20%\n";
	cout << "20-49" << setw(20) << "30%\n";
	cout << "50-99" << setw(20) << "40%\n";
	cout << "100 or more" << setw(14) << "50%\n" << endl;
	
	cout << "Enter quantity you would like to purchase: ";
	cin >> softwareQuantity;
	cout << fixed << setprecision(2);
	
	if(softwareQuantity > 0){
		if(softwareQuantity < 10){
			softwareDiscount = 1;
			softwareCost = (softwareQuantity * 99) * softwareDiscount;
	        cout << "You will pay a total of $" << softwareCost << endl;
		}
		else if(softwareQuantity >= 10 && softwareQuantity < 20){
			softwareDiscount = .8;
			softwareCost = (softwareQuantity * 99) * softwareDiscount;
	        cout << "You will pay a total of $" << softwareCost << endl;
		}
		else if(softwareQuantity >=20 && softwareQuantity < 50){
			softwareDiscount = .7;
			softwareCost = (softwareQuantity * 99) * softwareDiscount;
	        cout << "You will pay a total of $" << softwareCost << endl;
		}
		else if(softwareQuantity >= 50 && softwareQuantity < 100){
			softwareDiscount = .6;
			softwareCost = (softwareQuantity * 99) * softwareDiscount;
	        cout << "You will pay a total of $" << softwareCost << endl;
		}
		else if(softwareQuantity >= 100){
			softwareDiscount = .5;
			softwareCost = (softwareQuantity * 99) * softwareDiscount;
	        cout << "You will pay a total of $" << softwareCost << endl;
		}
	}
	else{
		cout << "Invalid entry!\n";
	}
	
	
	
	return 0;
}