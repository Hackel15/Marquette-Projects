#include <iostream>
using namespace std;

struct Money{
	double dollars;
	double cents;
};

struct Bills{
	Money savings;
	double bills;
	double balance;
};

Bills normalize(Bills& normal);
Bills balanced(Bills& total);

int main(){
	Bills myAccount;
	cout << "Enter dollar value in your account?\n";
	cin >> myAccount.savings.dollars;
	cout << "Enter cent value in your account?\n";
	cin >> myAccount.savings.cents;
	cout << "Enter total bills to be paid.\n";
	cin >> myAccount.bills;
	normalize(myAccount);
	balanced(myAccount);

	cout << "Total balance: $" << myAccount.balance << "." << myAccount.savings.cents;
	
	
	return 0;
}

Bills balanced(Bills& total){
	total.balance = total.savings.dollars - total.bills;
	return total;
	
}

Bills normalize(Bills& normal){

	while(normal.savings.cents >= 100){
		normal.savings.dollars += 1;
		normal.savings.cents -= 100;
	}	
	
	return normal;
}


