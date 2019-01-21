package gdc_lcm;
import java.util.Random;
import java.util.Scanner;

/**
 * Discrete Math
 * @author tyler
 * Dr. Tucker
 */
public class GDC_LCM {
        
    public static int gdc(int A, int B){
        if(A < B){
            int t = A;
            A = B;
            B = t;
        }
        System.out.printf("Value 1: %d \nValue 2: %d \n", A, B);
            
        int Q = A/B;
        int R = A%B;

        while(A != (B*Q)){
            A = B;
            B = R;
            Q = A/B;
            R = A%B;
        } 
        return B;
    }
        
    public static int lcm(int A, int B){
        int t = A > B ? A : B;
        while(!((t % A == 0) && (t % B == 0))){
           
            t++;
        }
        return t;
    }
    
    public static int getNumbers(){
        int x = 0;
        Scanner input = new Scanner(System.in);
        do{
            if(x < 0)
                System.out.println("Invalid number. Please enter positive integer.");
            System.out.print("Enter input value: ");
            x = input.nextInt();
        }while(x < 0);
        return x;
    }
    
        
    public static void main(String[] args) {
        int A, B, G_D_C, L_C_M;
        /*
        Random rand = new Random();
        A = rand.nextInt(50) + 50;
        B = rand.nextInt(50) + 1;
        */
        A = getNumbers();
        B = getNumbers();
        
        
        G_D_C = gdc(A,B);
        L_C_M = lcm(A,B);
        
        System.out.printf("GDC: %d\nLCM: %d\n", G_D_C, (G_D_C*L_C_M));
        System.out.println("Ending GDC_LCM Program.");
    }
}
