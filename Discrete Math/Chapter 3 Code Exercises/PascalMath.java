import java.util.Scanner;

public class PascalMath {
	
	public static int choose(int n, int r){
		int answer = 0;
		answer = (factorial(n))/(factorial(r)*factorial(n-r));
		return answer;
	}

	public static int factorial(int x){
		int answer = 1;
		for(int i = x; i > 0; i--){
			answer *= i;
		}
		return answer;
	}
	
	public static void main(String [] args){
		Scanner input = new Scanner(System.in);
		int rows = 0;
		int format = 0;
		System.out.print("Enter number of rows: ");
		rows = input.nextInt(); 
		while(rows <= 0){
			System.out.println("Invalid number!");
			System.out.print("Enter number of rows: ");
			rows = input.nextInt();
		}
		format = rows;
		String [] space = new String[format];
		space[0] = " ";
		for(int i = 1; i < format; i++){
			space[i] = space[i-1]+ " ";
		}
		
		for(int n = 0; n < rows; n++){
			System.out.print(space[format - 1]);
			for(int r = 0; r <= n; r++){
				System.out.printf("%d ", choose(n, r));
			}
			System.out.print("\n");
			format--;
			
		}
	
	}

}