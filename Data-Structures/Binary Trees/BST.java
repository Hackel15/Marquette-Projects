/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Nichole Turnage
 */
public class BST {
    public static  BSTNode root;
	public BST(){
		this.root = null;
	}
	
	public boolean find(int id){
		BSTNode current = root;
		while(current!=null){
			if(current.data==id){
				return true;
			}else if(current.data>id){
				current = current.left;
			}else{
				current = current.right;
			}
		}
		return false;
	}
	public boolean delete(int id){
		BSTNode parent = root;
		BSTNode current = root;
		boolean isLeftChild = false;
		//Case 1: The node isn't in the tree.
                while(current.data!=id){
			parent = current;
			if(current.data>id){
				isLeftChild = true;
				current = current.left;
			}else{
				isLeftChild = false;
				current = current.right;
                        }
			if(current ==null){
				return false;
			}
		}
		//if i am here that means we have found the node
		//Case 2: if node to be deleted has no children
		if(current.left==null && current.right==null){
			if(current==root){
				root = null;
			}
			if(isLeftChild ==true){
				parent.left = null;
			}else{
				parent.right = null;
			}
		}
		//Case 3: if node to be deleted has only one child
		else if(current.right==null){
			if(current==root){
				root = current.left;
			}else if(isLeftChild){
				parent.left = current.left;
			}else{
				parent.right = current.left;
			}
		}
		else if(current.left==null){
			if(current==root){
				root = current.right;
			}else if(isLeftChild){
				parent.left = current.right;
			}else{
				parent.right = current.right;
			}
		}
                //Case 4: The node has 2 children
                else if(current.left!=null && current.right!=null){
                 
			//now we have found the minimum element in the right sub tree
			BSTNode successor	 = getSuccessor(current);
			if(current==root){
				root = successor;
			}else if(isLeftChild){
				parent.left = successor;
			}else{
				parent.right = successor;
			}			
			successor.left = current.left;
		}		
		return true;		
	}
	
	public BSTNode getSuccessor(BSTNode deleteNode){
		BSTNode successsor =null;
		BSTNode successsorParent =null;
		BSTNode current = deleteNode.right;
		while(current!=null){
			successsorParent = successsor;
			successsor = current;
			current = current.left;
		}
		//check if successor has the right child, it cannot have left child for sure
		// if it does have the right child, add it to the left of successorParent.
                //successsorParent
		if(successsor!=deleteNode.right){
			successsorParent.left = successsor.right;
			successsor.right = deleteNode.right;
		}
		return successsor;
	}   
         public void insert(int id){
		BSTNode newBSTNode = new BSTNode(id);
		if(root==null){
			root = newBSTNode;
			return;
		}
		BSTNode current = root;
		BSTNode parent = null;
		while(true){
			parent = current;
			if(id<current.data){				
				current = current.left;
				if(current==null){
					parent.left = newBSTNode;
					return;
				}
			}else{
				current = current.right;
				if(current==null){
					parent.right = newBSTNode;
					return;
				}
			}
		}
	}
	public void inOrderdisplay(BSTNode root){
		if(root!=null){
			inOrderdisplay(root.left);
			System.out.print(" " + root.data);
			inOrderdisplay(root.right);
		}
	}
        
        public void preOrderdisplay(BSTNode root)
        {
            if(root != null){
                System.out.print(" " + root.data);
                preOrderdisplay(root.left);
                preOrderdisplay(root.right);
            }
        }
        
        public void postOrderdisplay(BSTNode root)
        {
            if(root != null)
            {
                preOrderdisplay(root.left);
                preOrderdisplay(root.right);
                System.out.print(" " + root.data);
            }
        }
        public static void main(String arg[]){
		BST b = new BST();
		b.insert(3);b.insert(8);
		b.insert(1);b.insert(4);b.insert(6);b.insert(2);
                b.insert(10);b.insert(9);
		b.insert(20);b.insert(25);b.insert(15);b.insert(16);
		System.out.println("Original Tree : ");
		b.inOrderdisplay(b.root);		
		System.out.println("");
		System.out.println("Check whether Node with value 4 exists : " 
                        + b.find(4));
		System.out.println("Delete Node with no children (2) : " 
                        + b.delete(2));		
		b.inOrderdisplay(root);
		System.out.println("\n Delete Node with one child (4) : " 
                        + b.delete(4));		
		b.inOrderdisplay(root);
		System.out.println("\n Delete Node with Two children (10) : " 
                        + b.delete(10));		
		b.inOrderdisplay(root);
                
                
	}
}

