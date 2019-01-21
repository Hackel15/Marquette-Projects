//import support.*;

/**
 * @author Praveen Madiraju
 *
 */
public class ShareDList<T> {

	protected ShareNode<T> header;
	protected ShareNode<T> trailer;

	protected int size;

	/**
	 * 
	 */
	public ShareDList() {
		header = null;
		trailer = null;
		size = 0;

	}

	/**
	 * @return the header
	 */
	public ShareNode<T> getHeader() {
		return header;
	}

	/**
	 * @return the trailer
	 */
	public ShareNode<T> getTrailer() {
		return trailer;
	}

	/**
	 * @return the size
	 */
	public int getSize() {
		return size;
	}

	// add element to the front of the list
	public void addToFront(T buyOrSell, T shares, T price) {
		ShareNode<T> newNode = new ShareNode<T>(buyOrSell, shares, price);

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
	public void addToLast(T buyOrSell, T shares, T price) {
		ShareNode<T> newNode = new ShareNode<T>(buyOrSell, shares, price);
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
//		ShareNode<T> node = header;
//		String result = "";
//		while(node!= null) {
//			result+=node.getInfo();
//			result+="<=>";
//			node = (DShareNode<T>)node.getLink();
//		}
//		result = result.substring(0,result.length()-3);
//		return result;
//	}
//
//	public void print() {
//		ShareNode<T> v = header;
//		while (v != null) {
//			System.out.println(v.getInfo());
//			v = (DShareNode) v.getLink();
//		}
//
//	}

	//2)	Define a recursive method, boolean search (T element) in DList 
	//class that returns true if the element is 
	// found in the double linked list.

	public ShareNode<T> search() {
		return search (header);
	}


	private ShareNode<T> search(ShareNode<T> node) {
		if(node == null)
			return null;
		if(node.getBuyOrSell().equals("sell"))
			return node;
		else
			return search((ShareNode<T>) node.getLink());

	}

	//Given the DList class, implement a void removeLast() method 
	//which removes the last node in the double linked list
	public void removeLast() {
		if (isEmpty()) 
			throw new IllegalStateException("cannot remove from empty DList");
		ShareNode<T> u = trailer.getBack();
		u.setLink(null);
		trailer = u;		
	}

	// implement stack operations void push(T element) and T pop()

//	public void push(T element) {
//		ShareNode<T> newNode = new ShareNode<T>(element);
//		addToLast(element);
//	}
//
//	public T pop() {
//		return null;
//	}
}