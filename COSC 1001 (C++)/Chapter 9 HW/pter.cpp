/*Sorts separate pointer array by address
  Keeps original array
**/

#include <string>
#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;
//prototypes
void arrSort(int* arr[], int size);
void displayarray(int arr[], int size);
void displayPtrArr(int* arr[], int size);

int main(){

	const int NUM_DONATIONS = 7;
	int dontations[NUM_DONATIONS] = {90, 25, 10, 5, 30, 40, 5};
	int* ptrSortedDonations[NUM_DONATIONS] = {0,0,0,0,0,0,0};
	
	for(int i = 0; i<NUM_DONATIONS; i++){
		ptrSortedDonations[i] = &dontations[i];
	}
	
	arrSort(ptrSortedDonations, NUM_DONATIONS);
	displayPtrArr(ptrSortedDonations, NUM_DONATIONS);
	displayarray(dontations, NUM_DONATIONS);
	
	

	return 0;
}

void arrSort(int* arr[], int size){
	int startScan, minIndex;
	int* minEle;
	
	for(startScan = 0; startScan < (size - 1); startScan++){
		minIndex = startScan;
		minEle = arr[startScan];
		for(int i = startScan + 1; i<size; i++){
			if(*(arr[i]) < *minEle){
				minEle = arr[i];
				minIndex = i;
			}
		}
		arr[minIndex] = arr[startScan];
		arr[startScan] =  minEle;
	}
	return;
	
}

void displayPtrArr(int* arr[], int size){
	cout << "Sorted pointer array: ";
	for(int i = 0; i<size; i++){
		cout << *(arr[i]) << " ";
	}
	cout << endl;
	return;
}

void displayarray(int arr[], int size){
	cout << "Original array: ";
	for(int i = 0; i<size; i++){
		cout << arr[i] << " ";
	}
	cout << endl;
	return;
}



