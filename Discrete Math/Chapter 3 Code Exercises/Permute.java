
import java.util.Scanner;

/**
 * Discrete Mathematics 
 * @author Tyler Hackel
 * Dr. Tucker
 */
public class Permute {

    public static long permute(long value){
        value *= (value-1);
        
        return value;
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        long nValue, answer, temp;
        final int two = 2;
        System.out.println("This program displays the permutation for n permutes 2:");
        System.out.print("Enter a value for n, where n > 1 & n <= 100: ");
        nValue = input.nextInt();
        while(nValue < 2 || nValue > 100 ){
            System.out.println("Invalid Number.. ");
            System.out.print("Enter a value for n, where n >= 2: ");
            nValue = input.nextInt();
        }
		temp = nValue;
		if(nValue > 15){
			System.out.print("The value entered will fill your entire screen with the solution.\n" +
			"Do you wish to see all resuts? Enter '1' for yes, '2' for no: ");
			answer = input.nextInt();
			while(!(answer == 1 || answer == 2 )){
				System.out.println("Invalid Number.. ");
				System.out.print("Enter '1' for yes, '2' for no: ");
				answer = input.nextInt();
			}
			if(answer == 2)
				nValue = 15;
		}
		int counter = 0;
		for(int i = 1; i <= nValue; i++){
			for(int j = 1; j <= nValue; j++){
				if(counter == 15){
					System.out.print("\n");
					counter = 0;
				}
				if(i == j){
					continue;
				}else{
					counter++;
					System.out.printf("(%d, %d) ", i, j);
				}
			}
		}
        
        answer = permute(temp);
        System.out.printf("%d permutes %d = %d \n", temp, two, answer);
        
    }
    
}
