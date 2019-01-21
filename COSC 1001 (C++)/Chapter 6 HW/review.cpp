//write a function prototype, that takes two double type parameters
// and return the differece

double calcDifferece(double number1, double number2); //prototype


//please implement a function definition, which has no formal parameters,
// and it returns the sum of two double variables.
// you should ask the user to input two double type variables.

double getSum(){
	double num1,
		   num2,
		   sum;
	cout << "Enter two numbers: ";
	cin >> num1 >> num2;
	sum = num1 + num2;
	return sum;
}

//next function
//two double formal parameters and returns sum
double getSum(double num1, double num2){
	double sum;
	sum = num1 + num2;
	return sum;
}

//next question
//use pass by referece to get sum
void getSum(double num1, double num2, double& sum){
	sum = num1 + num2;
	return;
}

//next question










