import java.util.Scanner; 

/**
 * Payload of this program.
 * The Record Class holds data to be retrieved.
 * @author tyler
 */

public class Record {
    /**
     * Instance variables for the class.
     */
    static private final String DUMMYSTIRNG = "Dummystring";
    static private final int DUMMYINT = Integer.MIN_VALUE;
    private int teaching;   //holds course taught
    private String name;    //holds name
    private String phoneNumber;        //holds phonenumber
    private String officeNumber;       //holds office number
    
    /**
     * Constructor
     * Assigns dummy variables to instance variables
     */
    public Record(){
        this.setName(Record.DUMMYSTIRNG);
        this.setOfficeNumber(Record.DUMMYSTIRNG);
        this.setPhoneNumber(Record.DUMMYSTIRNG);
        this.setTeaching(Record.DUMMYINT);
    }
    
    /**
     * Accessor method to get the <code>name</code>
     * @return the value of <code>name</code>
     */
    public String getName(){
        return this.name;
    }
    
    /**
     * Accessor method to get <code>officeNumber</code>
     * @return the value of <code>officeNumber</code>
     */
    public String getOfficeNumber(){
        return this.officeNumber;
    }
    
    /**
     * Accesor method to get <code>phoneNumber</code>
     * @return the value of <code>phoneNumber</code>
     */
    public String getPhoneNumber(){
        return this.phoneNumber;
    }
    
    /**
     * Accessor method to get <code>teaching</code>
     * @return the value of <code>teaching</code>
     */
    public int getTeaching(){
        return this.teaching;
    }
    
    /**
     * Mutator method to set <code>name</code>
     * @param that sets the value of <code>name</code>
     */
    private void setName(String that){
        this.name = that;
    }
    
    /**
     * Mutator method to set <code>officeNumber</code>
     * @param that sets the value of <code>officeNumber</code>
     */
    private void setOfficeNumber(String that){
        this.officeNumber = that;
    }
    
    /**
     * Mutator method to set the value <code>phoneNumber</code>
     * @param that sets the value of <code>phoneNumber</code>
     */
    private void setPhoneNumber(String that){
        this.phoneNumber = that;
    }
    
    /**
     * Mutator method to set the value of <code>teaching</code>
     * @param that sets the value of <code>teaching</code>
     */
    private void setTeaching(int that){
        this.teaching = that;
    }
    
    /**
     * Compares Record to determine if greater than, less than,
     * or equal to compared Record.
     * @param that used to compare against this record
     * @return value of three types:
     * -1 if less than
     * +1 if greater than
     * 0 if equal to
     */
    public int compareTo(Record that){
        if(this.getName().compareTo(that.getName()) < 0)
            return -1;
        else if (this.getName().compareTo(that.getName()) > 0)
            return +1;
        else
            return 0;
    }
    
    /**
     * readRecord method is used to read data from file and
     * set instance variables with read-in data.
     * @param inFile is the input file to store data
     */
    public void readRecord(Scanner inFile){
        int n;
        String s;
        if(inFile.hasNext()){
            s = inFile.next();
            this.setName(s);
            
            s = inFile.next();
            this.setOfficeNumber(s);
            
            s = inFile.next();
            this.setPhoneNumber(s);
            
            n = inFile.nextInt();
            this.setTeaching(n);            
        }
    }
    
    /**
     * toString method converts Record data into String type
     * @return s of type String
     */
    public String toString(){
        String s;
        s = String.format("%-10s %s %s %4d", this.getName(), 
                    this.getOfficeNumber(), this.getPhoneNumber(),
                    this.getTeaching());
        return s;
    }
}
