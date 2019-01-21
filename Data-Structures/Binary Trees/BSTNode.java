/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Nichole Turnage
 */
public class BSTNode {
    
    int data;
    BSTNode left;
    BSTNode right;
    
    public BSTNode(int d)
    {
        this.data = d;
        left = null;
        right = null;
    }
    
    public void setData(int d)
    {
        this.data = d;
    }
    
    public int getData()
    {
        return data;
    }
    
}
