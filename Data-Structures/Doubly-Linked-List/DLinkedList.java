
/**
 * Data Structure of this program.
 * This orders the data in a doubly linked list
 * @author tyler
 */
public class DLinkedList{
        
        /**
         * Instance variables for class
         */
	private Link firstLink;//holds value of first link
	private final Link lastLink;//holds value of null
        private int size; 
	
        /**
        * Constructor.
        * Initialize firstLinnk to null
        * Initialize lastLink to a new link with null data
        * Initialize size to zero
        */
	DLinkedList(){
		firstLink = null;
		lastLink = new Link(null);
                size = 0;
	}
        
        /**
         * This method increments the number of linked lists by one
         * This does not include the lastLink
         */
        private void incrementSize(){
            size++;
        }
        
        /**
         * This method decrements the number of linked lists by one
         */
        private void decrementSize(){
            size--;
        }
        
        /**
         * isEmpty method is used to determine an empty linked list
         * @return boolean type
         */
        private boolean isEmpty(){
            boolean set = false;
            if(size == 0)
                set = true;
            return set;
        }
        
        /**
         * addLink method creates a new link of data
         * @param data is stored in a new link
         */
        public void addLink(Record data){
            if(isEmpty()){
                Link temp = new Link(data);
		firstLink = temp;
		firstLink.setNext(lastLink);
                firstLink.setPrev(null);
                lastLink.setPrev(firstLink);
                incrementSize();
            }else{
                Link temp = new Link(data);
                temp.setNext(firstLink);
                firstLink.setPrev(temp);
                firstLink = temp;
                incrementSize();
                insertSort();
            }
        }
        
        /**
         * printLinks returns a string of the records
         * @return s
         */
        public String printLinks(){
            String s = "";
            Link temp = firstLink;
            while(temp != lastLink){
                s += temp.returnData().toString() + "\n";
                temp = temp.getNext();
            }
            return s;
        }
        
        /**
         * removeLink method removes a specified link, if found.
         * @param delete is a string name, found in a Record
         * @return is 
         * false is returned if link is not found
         * true is returned if link is found and removed
         */
        public boolean removeLink(String delete){
            Link temp = firstLink;
            
            boolean is = false;
            while(temp.getNext() != null){
		if(temp.returnData().getName().compareTo(delete) == 0){
                    //delete here (swaping nodes)
                    is = true;
                    decrementSize();
                    if(temp.getPrev() == null){
                        firstLink = temp.getNext();
                        //firstLink.setPrev(null);
                        break;
                    }else if(temp.getNext() == null){
                        temp.getPrev().setNext(temp.getNext());
                        break;
                    }else{
                        temp.getPrev().setNext(temp.getNext());
                        temp.getNext().setPrev(temp.getPrev());
                        break;
                    }
                }
                temp = temp.getNext();
            }
            return is;
        }
        
        /**
         * insortSort method sorts the newly inserted link
         */
        private void insertSort(){
            Link first = firstLink;
            Link next = first.getNext();
            
            while(next != lastLink){
                if(first.returnData().getName().compareTo(next.returnData().getName()) >= 0){
                    Record temp;
                    temp = first.returnData();
                    first.setData(next.returnData());
                    next.setData(temp);
                    
                    first = next;
                    next = first.getNext();
                }else{
                    //System.out.println("break");
                    break;
                }
            }
        }   
    }