package matrixaddition;


/**
 * Discrete Math
 * @author tyler
 * Dr. Tucker
 */

public class MatrixAddition {
    
    public static void main(String[] args) {
        MyMatrixClass matrix1 = new MyMatrixClass();
        MyMatrixClass matrix2 = new MyMatrixClass();
        int[][] addedMatrix;
        matrix1.setNewMatrix();
        matrix2.setNewMatrix();
        
        
        if(matrix1.getComparison(matrix2.getCol()*matrix2.getRow())){
            System.out.println("Matrixcies are EQUAL in size.");
            matrix1.displayMatrix();
            matrix2.displayMatrix();
            matrix1.addMatrix(matrix2.getMatrix());
            matrix1.displaySumOfMatrix();
            matrix1.multiplyMatrix(matrix2);
       
        }
        else{
            System.out.println("Matrixcies are NOT equal in size.");
            System.out.println("Ending Program.");
        }
        
 
    }
    
}
