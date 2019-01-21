//Chapter 8 HW Q6
#include <iostream>
#include <string>
using namespace std;

//prototypes
void displayNames(const string array[], int size);
void sortNames(string array[], int size);

int main()
{
	//variables
	const int NUM_NAMES = 20;
	string names[NUM_NAMES] = {"Collins, Bill", "Smith, Bart", "Allen, Jim",
                               "Griffin, Jim", "Stamey, Marty", "Rose, Geri",
                               "Taylor, Terri", "Johnson, Jill", "Allison, Jeff",
                               "Looney, Joe", "Wolfe, Bill", "James, Jean",
                               "Weaver, Jim", "Pore, Bob", "Rutherford, Greg",
                               "Javens, Renee", "Harrison, Rose", "Setzer, Cathy",
                               "Pike, Gordon", "Holland, Beth" };

	displayNames(names, NUM_NAMES);
	sortNames(names, NUM_NAMES);
	displayNames(names, NUM_NAMES);

	return 0;
}

//display names
void displayNames(const string array[], int size){
	for(int i=0; i<size; i++){
		cout << array[i] << endl;
	}
	cout << endl << endl;
	
	return;
}

//sort names by selection
void sortNames(string array[], int size){
	
	string minName;
	int minIndex;
	for(int start = 0; start < (size - 1); start++){
		minName = array[start];
		minIndex = start;
		for(int i = start + 1; i < size; i++){
			if(array[i] < minName){
				minName = array[i];
				minIndex = i;
			}
		}
		array[minIndex] = array[start];
		array[start] = minName;
	}
	return;
}