//Linear Search
int searchList(const int list[], int numElem, int value){
	int index=0;
	int position=-1;
	bool found=false;
	while(index < numElem && !found){
		if(list[index]== value){
			found = true;
			position = index;
		}
		index++;
	}
	return position;
}

for(int i=0; i<numEle; i++){
	if(list[index]==value){
		found = true;
		position = index;
	}
}

//Binary Search
int binarySearch(const int list[], int numElem, int value){
	int first=0,
		last=numElem-1,
		middle,
		postion=-1;
		for(int i=0; i<numElem; i++){
			middle = (first+last)/2;
			if(list[middle]==value){
				position = middle;
				break;
			}
			else if(list[middle]>value){
				last = middle -1;
			}
			else{
				first = middle +1;
			}
		}
	return postion;
	
}