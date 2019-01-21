#include <iostream>
using namespace std;

int main(){
	int size = 8;
	int* numbers[size];
	cout << "Enter numbers:\n ";
	for(int i = 0; i<size; i++){
		cout << "Number " << i+1; << ": ";
		cin >> *(numbers[i]);
	}
	int mode;
	int freq;
	for(int i = 0; i< size; i++){
			mode = *(numbers[i]);
			freq = 0;
		for(int j = 0; j< size; j++){
			if(*(numbers[j]) == mode){
				freq++;
			}
		}
	}
	
}