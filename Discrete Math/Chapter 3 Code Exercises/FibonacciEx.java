import java.util.Scanner;
import java.lang.Math;
/**
 * Discrete Mathematics 
 * @author Tyler Hackel
 * Dr. Tucker
 */
public class FibonacciEx {

    public static long permute(long value){
        value *= (value-1);
        
        return value;
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int nValue;
		double answer;
		
        System.out.println("This program displays the Fibonacci sequence for n values:");
        System.out.print("Enter a value for n, where n > 0 and n < 45: ");
        nValue = input.nextInt();
        while(nValue < 1 || nValue > 44){
            System.out.println("Invalid Number.. ");
            System.out.print("Enter a value for n, where n > 0: ");
            nValue = input.nextInt();
        }
		
		answer = (1/Math.sqrt(5))*Math.pow(((1+Math.sqrt(5))/2), nValue) - (1/Math.sqrt(5))*Math.pow(((1-Math.sqrt(5))/2), nValue);
		
		System.out.print(Math.round(answer));
		
        
    }
    
}
