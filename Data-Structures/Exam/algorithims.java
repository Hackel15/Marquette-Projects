static class Algorithims{
        public void bubbleSort(){
            int [] myArray = {2,49,22,44,9,8,2,4};
            int size = myArray.length;
            int lowerSub = 0, upperSub = size-1, midSub;
            int minVal, minInd, temp;
            for(int start = 0; start < size-1; start++){
                minInd = start;
                minVal = myArray[start];
                for(int j = start+1; j<size; j++){
                    if(myArray[j] < minVal){
                        minInd = j;
                        minVal = myArray[j];
                    }
                }
                temp = myArray[minInd];
                myArray[minInd] = myArray[start];
                myArray[start] = temp;
            }
            
            for(int i = 0; i < size; i++){
                System.out.print(myArray[i] + " ");
            }
        }
        
        public void sequentialSearch(){
            int [] myArray = {1, 2, 3, 4, 5};
            int key = 3;
            int counter = 0;
            while(counter < myArray.length){
                if(key == myArray[counter])
                    System.out.println("FOUND: " + myArray[counter]);
                counter++;
            }
        }
        
        public void binarySearch(){
            int [] myArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
            int returnValue = -1, lowerSub = 0, midSub;
            int key = 5, upperSub = myArray.length -1;
            midSub = (lowerSub+upperSub)/2;
            while(lowerSub < upperSub){
                if(key > midSub)
                    lowerSub = midSub+1;
                else if(key < midSub)
                    upperSub = midSub-1;
                else{
                    returnValue = midSub;
                    break;
                }
                midSub = (lowerSub+upperSub)/2;
            }
            
            System.out.println("KEY: " + key + " FOUND VALUE: "+ returnValue);
        }
		
		public void insertionSort(){
			//Assuming Array List is initialized to myArra and already
			//sorted from least to greatest.
			/**
			int temp = 0;
			myArray.add(1);
			for(int last = myArray.size()-1; last > 0; last--){
				if(myArray.get(last) <= myArray.get(last-1)){
					temp = myArray.get(last);
					myArray.set(last, myArray.get(last-1);
					myArray.set(last-1, temp);
				}else{
					break;
				}
			}
			*/
		}
    }