package matrixaddition;
import java.util.Scanner;

/**
 * Discrete Math
 * @author tyler
 * Dr. Tucker
 */

public class MyMatrixClass {
    private int row;
    private int col;
    private int[][] matrix;
    private int[][] sumOfMatrix;
    private int [][] productMatrix;
    private int num;
    static int count;
    
    public MyMatrixClass(){
        count++;
        num = count;
    }
    
    
    public void multiplyMatrix(MyMatrixClass product){
        int holdValue = 0, t=0;
        if(this.getCol() == product.getRow()){
            productMatrix = new int[this.getRow()][product.getCol()];
            //start here
            for (int i = 0 ; i < this.getRow() ; i++){
                for (int j = 0 ; j < product.getCol() ; j++){   
                    for (int k = 0 ; k < product.getRow() ; k++){
                         holdValue += (this.matrix[i][k])*(product.matrix[k][j]);
                    }
                    productMatrix[i][j] = holdValue;
                    holdValue = 0;
                }
            }
      
            System.out.println("\nProduct of Matrices");
            for(int i = 0; i < this.getRow(); i++){
                for(int j = 0; j< product.getCol(); j++){
                    System.out.printf("%d  ", productMatrix[i][j]);
                }
                System.out.print("\n");
            }
            System.out.println();
        }
        else{
            System.out.println("Rows of Matrix 1 does not match the columns"
                    + "of Matrix 2.\n Ending Program.");
            System.exit(1);
        }
    }
            
    public void addMatrix(int[][] m2){
        sumOfMatrix = new int[row][col];
        for(int i = 0; i < row; i++){
            for(int j = 0; j<col; j++){
                sumOfMatrix[i][j] = (matrix[i][j] + m2[i][j]);
            }
        }
    }
    
    public void displaySumOfMatrix(){
        
        System.out.println("\nSum of Matrices");
        for(int i = 0; i < row; i++){
            for(int j = 0; j< col; j++){
                System.out.printf("%d  ", sumOfMatrix[i][j]);
            }
            System.out.print("\n");
        }
        System.out.println();
    }
    
    public void displayMatrix(){
        
        System.out.printf("\nMatrix %d\n", num);
        for(int i = 0; i < row; i++){
            for(int j = 0; j< col; j++){
                System.out.printf("%d  ", matrix[i][j]);
            }
            System.out.print("\n");
        }
        System.out.println();
    }
    
    public boolean getComparison(int that){
  
        if(this.row*col == that)
            return true;
        else
            return false;
    }
    
    public int getRow(){
        return row;
    }
    
    public int getCol(){
        return col;
    }
    
    public int[][] getMatrix(){
        return matrix;
    }
    
    public void setNewMatrix(){
        Scanner input = new Scanner(System.in);
        int[][] newMatrix;
        int x = 0, y = 0;
        System.out.print("\n");
        do{
            if(x < 0 || y < 0)
                System.out.println("Invalid number. Please enter positive integer.");
            System.out.printf("Enter number of rows for matrix %d: ", num);
            x = input.nextInt();
            System.out.printf("Enter number of columns for matrix %d: ", num);
            y = input.nextInt();
        }while(x < 0 || y < 0);
        System.out.print("\n");
        row = x;
        col = y;
        newMatrix = new int[x][y];
        System.out.printf("Enter values to fill your matrix of %d rows and"
                + " %d columns.\n", x, y);
        for(int i = 0; i < x; i++){
            for(int j = 0; j < y; j++){
                System.out.printf("Enter value for row %d column %d: ", 
                        i+1, j+1);
                newMatrix[i][j] = input.nextInt();
            }   
        }
        System.out.print("\n");
        matrix = newMatrix;
    }
}
