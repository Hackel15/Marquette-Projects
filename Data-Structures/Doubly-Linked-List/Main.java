import java.util.Scanner;

/**
 * Computer Science II
 * @author Tyler Hackel
 * Doubly Linked List
 */
public class Main {
    public static void main(String [] args){
        String inFileName = null;//file name
        FlatFile flat;
        
        Scanner inFile = null;//inFile for input data
        Scanner input = new Scanner(System.in);//user input
        
        
        
        //Input desired input file
        System.out.print("Enter desired input file: ");
        inFileName = input.next();
        inFile = FileUtils.ScannerOpen(inFileName);
        
       
        System.out.println("Reading data in from: " + inFileName);
        flat = new FlatFile();
        flat.readFile(inFile);
        
        System.out.println("Closing file: " + inFileName);
        inFile.close();
        
        System.out.println("Printing links");
        System.out.println(flat.toString());
        System.out.println("Removing LINK: Luxemburg & Farley ");
        flat.removeRec("Luxemburg");
        flat.removeRec("Farley");
        System.out.println(flat.toString());
        
        Record testRec = new Record();
        System.out.println("Inserting and sorting Dummy Record record");
        flat.addRec(testRec);
        System.out.println(flat.toString());
        
    }
     
}

