//import support.*;

/**
 * @author Praveen Madiraju
 *
 */
public class DList<T> {

	protected LLNode<T> header;
	protected LLNode<T> trailer;

	protected int size;

	/**
	 * 
	 */
	public DList() {
		header = null;
		trailer = null;
		size = 0;

	}

	/**
	 * @return the header
	 */
	public LLNode<T> getHeader() {
		return header;
	}

	/**
	 * @return the trailer
	 */
	public LLNode<T> getTrailer() {
		return trailer;
	}

	/**
	 * @return the size
	 */
	public int getSize() {
		return size;
	}

	// add element to the front of the list
	public void addToFront(T title, T abbreviation) {
		LLNode<T> newNode = new LLNode<T>(title, abbreviation);

		if (header == null) {
			header = newNode;
		}
		if (trailer == null)
			trailer = newNode;
		else {
			newNode.setLink(header);
			header.setBack(newNode);
			header = newNode;
		}
		size++;

	}

	// add element to the end of the list
	public void addToLast(T title, T abbreviation) {
		LLNode<T> newNode = new LLNode<T>(title, abbreviation);
		newNode.setLink(null);

		if (trailer == null) {
			trailer = newNode;
			header = newNode;
		} else {
			trailer.setLink(newNode);
			newNode.setBack(trailer);
			trailer = newNode;
		}
		size++;
	}

	public boolean isEmpty() {
		return header == null;
	}

//	public String toString() {
//		
//	}
//
	public void print() {
		LLNode<T> v = header;
		while (v != null) {
			System.out.println(v.getTitle() + " " + v.getAbb());
			ShareNode<T> s = v.getTransactions().header;
			while(s != null){
				System.out.println(s.getBuyOrSell() + " " + s.getShares() + " " + s.getPrice());
				s = s.getLink();
			}
			v = v.getLink();
		}

	}

	//2)	Define a recursive method, boolean search (T element) in DList 
	//class that returns true if the element is 
	// found in the double linked list.

	public LLNode<T> search(T abbreviation) {
		return search (header,abbreviation);
	}


	private LLNode<T> search(LLNode<T> node, T abbreviation) {
		if(node == null)
			return null;
		if(node.getAbb().equals(abbreviation))
			return node;
		else
			return search((LLNode<T>) node.getLink(),abbreviation);

	}

	//Given the DList class, implement a void removeLast() method 
	//which removes the last node in the double linked list
	public void removeLast() {
		if (isEmpty()) 
			throw new IllegalStateException("cannot remove from empty DList");
		LLNode<T> u = trailer.getBack();
		u.setLink(null);
		trailer = u;		
	}

	// implement stack operations void push(T element) and T pop()

//	public void push(T element) {
//		LLNode<T> newNode = new LLNode<T>(element);
//		addToLast(element);
//	}
//
//	public T pop() {
//		return null;
//	}
}