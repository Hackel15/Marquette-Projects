//----------------------------------------------------------------------------
// LLNode.java            by Dale/Joyce/Weems                  Chapter 3
//
// Implements <T> nodes for a Linked List.
//----------------------------------------------------------------------------

public class LLNode<T>
{
	private LLNode<T> link;
	private ShareDList<T> transactions;
	private T title;
	private T abbreviation;
	private LLNode<T> back;


	public LLNode(T title, T abbreviation)
	{
		setAbb(abbreviation);
		setTitle(title);
		transactions = new ShareDList<T>();
		link = null;
		back = null;

	}
	
	public double calc() {
		double gainOrLoss = 0.0;
		
		ShareNode<T> sellNode = transactions.search();
		if(sellNode == null)
		{
			gainOrLoss = 0.0;
		}
		else if (transactions.header == sellNode)
		{
			 return null;
		}
		else
		{
			int numShares = (int) sellNode.getShares();
			String dollars = (String) sellNode.getPrice();
			double price = Double.valueOf(dollars.substring(1));
			
			
			
		}
		return gainOrLoss;
	}

	public void setTransactions(ShareDList<T> transactions)
	// Sets info of this LLNode.
	{
		this.transactions = transactions;
	}

	public ShareDList<T> getTransactions()
	// Returns info of this LLONode.
	{
		return transactions;
	}

	public void setTitle(T title)
	// Sets info of this LLNode.
	{
		this.title = title;
	}

	public T getTitle()
	// Returns info of this LLONode.
	{
		return title;
	}
	
	public void setAbb(T abbreviation)
	// Sets info of this LLNode.
	{
		this.abbreviation = abbreviation;
	}

	public T getAbb()
	// Returns info of this LLONode.
	{
		return abbreviation;
	}

	public void setLink(LLNode<T> link)
	// Sets link of this LLNode.
	{
		this.link = link;
	}

	public LLNode<T> getLink()
	// Returns link of this LLNode.
	{
		return link;
	}

	public void setBack(LLNode<T> back)
	// Sets back link of this DLLNode.
	{
		this.back = back;
	}

	public LLNode getBack()
	// Returns back link of this DLLNode.
	{
		return back;
	}
}

