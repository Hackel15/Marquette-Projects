public class Link{
	
        /**
         * Instance variables
         */
	private Record data;//data stored
	private Link next;//next link stored
	private Link prev;//previous link stored
	
        /**
         * Constructor
         * @param that initializes data
         */
	Link(Record that){
		this.data = that;
	}
	
        /**
         * Mutator method that sets next link 
         * @param that 
         */
	public void setNext(Link that){
		this.next = that;
	}
	
        /**
         * Mutator method that sets previous link
         * @param that 
         */
	public void setPrev(Link that){
		this.prev = that;
	}
        
        /**
         * Mutator method that sets data
         * @param that 
         */
        public void setData(Record that){
            this.data = that;
        }
	
        /**
         * Accessor method that gets next link
         * @return this.next
         */
	public Link getNext(){
		return this.next;
	}
	
        /**
         * Accessor method that gets next link
         * @return this.prev
         */
	public Link getPrev(){
		return this.prev;
	}
	
        /**
         * Accessor method that gets next link
         * @return data
         */
	public Record returnData(){
		return data;
	}

}