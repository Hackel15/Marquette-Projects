import java.util.Scanner;

/**
 * Discrete Mathematics 
 * @author Tyler Hackel
 * Dr. Tucker
 */
public class Fibonacci {

    public static long permute(long value){
        value *= (value-1);
        
        return value;
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int nValue;
        System.out.println("This program displays the Fibonacci sequence for n values:");
        System.out.print("Enter a value for n, where n > 0: ");
        nValue = input.nextInt();
        while(nValue < 1){
            System.out.println("Invalid Number.. ");
            System.out.print("Enter a value for n, where n > 0: ");
            nValue = input.nextInt();
        }
		
		long first = 1;
		long second = 1;
		long next = 0;
		
		for(int i = 0; i < nValue; i++){
			if(i < 2){
				System.out.print(first+", ");
			}else{
				if(i%10 == 0){
					System.out.print("\n");
				}
				next = first+second;
				if(i == nValue-1){
					System.out.print(next + ".");
					break;
				}
				System.out.print(next + ", ");
				second = first;
				first = next;
			}	
		}
        
    }
    
}
