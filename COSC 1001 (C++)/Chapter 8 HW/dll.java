

public class DLinkedList{

	private Link firstLink;
	private final Link lastLink;
        private int size; 
	
	DLinkedList(){
		firstLink = null;
		lastLink = null;
                size = 0;
	}
        
        private void incrementSize(){
            size++;
        }
        
        private boolean isEmpty(){
            boolean set;
            if(size == 0)
                set = true;
            else
                set = false;
            return set;
        }
        
        public void addLink(Record data){
            if(isEmpty()){
                Link temp = new Link(data);
		firstLink = temp;
		firstLink.setNext(lastLink);
                incrementSize();
            }else{
                Link temp = new Link(data);
                firstLink.setPrev(temp);
                temp.setNext(firstLink);
                firstLink = temp; 
                incrementSize();
            }
        }
        
        public void printLinks(){
            Link temp = firstLink;
            while(temp != null){
                System.out.println(temp.returnData().toString());
                temp = temp.getNext();
            }
        }
        
        public boolean removeLink(String delete){
            Link temp = firstLink;
            
            boolean is = false;
            while(temp != null){
		if(temp.returnData().getName().compareTo(delete) == 0){
                    //delete here (swaping nodes)
                    is = true;
                    if(temp.getPrev() == null){
                        firstLink = temp.getNext();
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
        
        public void insertSortLink(Record data){
            
            addLink(data);
            Link first = firstLink;
			Link temp = new Link();
            
           
            
            while(first.returnData().getName().compareTo(first.getNext().returnData().getName() <= 0){
                
				
                if(first.getPrev() == null){
					temp = first.getNext();
					first.setPrev(first.getNext());
					first.getNext().setPrev(null);
					first.setNext(first.getNext().getNext());
					first.getNext().getNext().setPrev(first);
					temp.getNext().setNext(temp); 
		
					
				}else if(first.getNext() == null){
					temp = first.getNext();
					first.setPrev(first.getNext());
					first.getNext().setPrev(first.getPrev);
					first.setNext(lastLink);
					temp.getNext().setNext(temp);
				
				}
				else{
					temp = first.getNext();
					first.setPrev(first.getNext());
					first.getNext().setPrev(first.getPrev);
					first.setNext(first.getNext().getNext());
					first.getNext().getNext().setPrev(first);
					temp.getNext().setNext(temp); 
				}
                
                first = first.getNext();
                
            }
            
        }
        
}