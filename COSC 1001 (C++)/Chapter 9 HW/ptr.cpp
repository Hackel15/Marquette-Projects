#include <string>
#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;
//prototypes
int* getrandom(int, double*);
string* getNames(int);

int main(){
	int size = 3;
	int* numbers = 0;
	double decade = 10;

	numbers = getrandom(size, &decade);

	string* names = 0;
	int nums[] = {1,2,3,4,5};
	int* test[] = {0,0,0,0,0};
	test[0] = &nums[0];
	
	cout << *(test[0]) << endl;

	names = getNames(size);

	for(int i=0; i< size; i++){
		cout << names[i] << " is ";
		cout << numbers[i] << " years old." << endl;
	}

	delete [] names;
	names = 0;
	delete [] numbers;
	numbers = 0;

	return 0;
}

string* getNames(int size){
	string* point = 0;

	point = new string[size];

	for(int i = 0; i<size; i++){
		cout << "Enter name " << i+1 << ":";
		getline(cin, point[i]);
	}
	return point;
}

int* getrandom(int size, double* decadesLived){
	int* point = 0;

	if(size <= 0){
		return 0;
	}

	point = new int[size];

	srand(time(0));
	for(int i = 0; i< size; i++){
		point[i] = (rand() % 9 + 0);
	}
	for(int i = 0; i< size; i++){
		point[i] *= *decadesLived;
	}

	return point;
}