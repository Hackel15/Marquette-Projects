//Review for Exam #4

#include <iostream>
#include <string>
using namespace std;

int main(){
	/**
	//Chapter 7
	/**
	1) write one line of code to declare a double type array named scores,
	then initialize it with these values: 95.5, 97, 87.5, 98
	*/
	//int size = 4;
	//double scores[size] = {95.5, 97, 87.5, 98};
	
	/**
	2) use a for loop to output the elements in the above array, with one element perline
	*/
	//for(int i = 0; i < size; i++){
	//	cout << scores[i] << endl;
	//}
	
	/**
	3) use a do - while loop to output the elements in the above array, with
	all elements in oneline, separated by a space.
	*/
	do{
		cout << scores << "\t";
		i++;
		
	}while(i < size);
	
	/**
	4)	use a while loop to calculate the average of the above array.
	*/
	int i=0,
		sum =0,
		average;
	while(i < 4){
		sum += scores[i];
		i++;
	}
	average = sum / 4;
	cout << "The avearge is " << average;
	
	/**
	5) use a for loop to find the smallest element in above array
	and then output smallest value;
	*/
	int minVal = scores[0];
	for(int a = 1; a < 4, a++){
		if(scores[a] < minVal){
			minVal = scores[a];
		}
	}
	cout << "Smallest value is " << minVal;
	/**
	6) What is wrong with the statement below?
	
	int numbers[] = {1, 2};
	cout << numbers[2];  // the index only goes to 1.
	*/
	
	//Chapter 8
	/**
	1) anything wrong with the statement bleow?  search is a search function. 
	
	int index = search(scores, 98); // needs size of elements
	*/	
	int index = search(scores, 4, 98);
	
	/**
	2) given the scores array defined above, can we apply a binary search?
	*/
		no, they need to be ordered/sorted.
	
	/**
	3) given the scores array defined above, then what statement should we put in under the 
	if branch: assume first, last, and middle are defined
	*/
	if(array[middle] > value){
		//what statement should we place here?
		first = middle + 1; 
	}
	
	//Chapter 10
	/**
	10) write two lines of statement, 
		first declare string variable named title, and initialize "System Engineer". 
		Second, output the third character of string. 
		Third, output the position of the character 'm' in the string. 
		forth, if total number of characters is > 30, output "too lengthy!"; otherwise, ouput: normal.
		fith, creat and output a substring of title, starting from the first character of 'e'.
		sixth, creat and output a substring of title, starting from the second character of 'e'.
	*/
	*/
	string title = "System Engineer";
	cout << title[2]; 
	
	/**
	int pos = title.find('m', 0);
	cout << "The position of 'm' is: " << pos;
	
	int size = title.size();
	if(size > 30){
		cout << "Too lengthy";
	}
	else{
		cout << "normal";
	}
	cout << title.substr(title.find('e')) << endl;
	*/
	
	int pos = title.find('e');
	cout << title.substring(title.find('e', pos + 1)) << endl;
	/**
	11) 
	*/
	
	return 0;
}









