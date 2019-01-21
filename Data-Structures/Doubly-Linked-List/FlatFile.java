
import java.util.Scanner;


/**
 * Computer Science II
 * @author tyler
 */
public class FlatFile {
    /**
     * Instance variables
     */
    private DLinkedList DLL;
    
    /**
     * Constructor is used to initialize a doubly linked list
     */
    public FlatFile(){
        DLL = new DLinkedList();
    }
    
    /**
     * removeRec method is used to remove a record from a doubly linked list
     * @param remove of string data type to search for record name.
     * @return results false if not found, true if removed.
     */
    public boolean removeRec(String remove){
        boolean results;
        results = DLL.removeLink(remove);
        return results;
    }
    
    /**
     * addRec method adds a record to a doubly linked list
     * @param rec is a Record 
     */
    public void addRec(Record rec){
        DLL.addLink(rec);
    }
   
    /**
     * readFile method is used to read records and create links of the records
     * @param inFile 
     */
    public void readFile(Scanner inFile){
        while(inFile.hasNext()){
            Record rec = new Record();
            rec.readRecord(inFile);
            DLL.addLink(rec);
        }
    }
    
    /**
     * toString method formats Record data into one String 
     * @return s for System Output
     */
    public String toString(){
        String s;
        s = DLL.printLinks();
        return s;
    }
    
}
