//----------------------------------------------------------------------------
// LLNode.java            by Dale/Joyce/Weems                  Chapter 3
//
// Implements <T> nodes for a Linked List.
//----------------------------------------------------------------------------

public class ShareNode<T>
{
  private ShareNode<T> link;
  private ShareNode<T> back;
  private T buyOrSell;
  private T shares;
  private T price;
  
  public ShareNode(T buyOrSell, T shares, T price)
  {
	setBuyOrSell(buyOrSell);
    setShares(shares);
    setPrice(price);
    link = null;
    back = null;

  }
  
  public void setBack(ShareNode<T> back)
  // Sets back link of this DLLNode.
  {
    this.back = back;
  }

  public ShareNode getBack()
  // Returns back link of this DLLNode.
  {
    return back;
  }
 
  public void setShares(T shares)
  // Sets info of this LLNode.
  {
    this.shares = shares;
  }

  public T getShares()
  // Returns info of this LLONode.
  {
    return shares;
  }
  
  public void setPrice(T price)
  // Sets info of this LLNode.
  {
    this.price = price;
  }

  public T getPrice()
  // Returns info of this LLONode.
  {
    return price;
  }
  
  public void setBuyOrSell(T buyOrSell)
  // Sets info of this LLNode.
  {
    this.buyOrSell = buyOrSell;
  }

  public T getBuyOrSell()
  // Returns info of this LLONode.
  {
    return buyOrSell;
  }
 
  public void setLink(ShareNode<T> link)
  // Sets link of this LLNode.
  {
    this.link = link;
  }

  public ShareNode<T> getLink()
  // Returns link of this LLNode.
  {
    return link;
  }
}
 
 