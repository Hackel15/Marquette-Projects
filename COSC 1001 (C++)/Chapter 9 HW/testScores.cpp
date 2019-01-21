#include <iostream>
#include <iomanip>

using namespace std;

//prototypes
double* enterTests(int size);
void displayTests(double* ptr, int size);
void sortTests(double* ptr[], int size);
double averageTests(double* ptr[], int size);
void displayTests(double* ptr[], int size);

int  main(){
	int number_of_tests = 0;
	double* tests = 0;
	
	cout << "Enter number of tests: ";
	cin >> number_of_tests;
	
	if(number_of_tests == 0){
		cout << "No tests to average!\n";
		cout << "Now ending program!\n";
		return 0;
	}
	
	tests = enterTests(number_of_tests);
	//displayTests(tests, number_of_tests);
	
	double* arrTest[number_of_tests] = {0};
	for(int i = 0; i<number_of_tests; i++){
		arrTest[i] = (tests + i);
	}
	sortTests(arrTest, number_of_tests);
	displayTests(arrTest, number_of_tests);

	cout << fixed << setprecision(2) << "Average = " << averageTests(arrTest, number_of_tests) << endl;
	
	delete [] tests;
	
	return 0;
}

double* enterTests(int size){
	double* ptr = 0;
	ptr = new double[size];
	
	cout << "Enter test scores:\n";
	for(int i=0; i<size;i++){
		cout << "Test " << i+1 << ":";
		cin >> ptr[i];
	}
	
	
	return ptr;
}

void displayTests(double* ptr, int size){
	for(int i = 0; i<size; i++){
		cout << "Test " << i+1 << ": " << ptr[i] << endl;
	}
	cout << endl;
	return;
}

void displayTests(double* ptr[], int size){
	cout << endl;
	cout << "Sorted scores:\n";
	for(int i = 0; i<size; i++){
		cout << "Test " << i+1 << ": " << *(ptr[i]) << endl;
	}
	cout << endl;
	return;
}

void sortTests(double* ptr[], int size){
	int startScan, minIndex;
	double* minEle = 0;
	for(startScan = 0; startScan<(size-1); startScan++){
		minEle = ptr[startScan];
		minIndex = startScan;
		for(int i = startScan + 1; i<size; i++){
			if(*(ptr[i]) < *minEle){
				minEle = ptr[i];
				minIndex = i;
			}
		}
		ptr[minIndex] = ptr[startScan];
		ptr[startScan] = minEle;
	}
	//cout << *(ptr[0]) << endl;
	return;
}


double averageTests(double* ptr[], int size){
	double sum = 0;
	for(int i = 1; i<size; i++){
		sum += *(ptr[i]);
	}
	return (sum / (size-1));
}




