package matrixaddition;


/**
 * Discrete Math
 * @author tyler
 * Dr. Tucker
 */

public class MatrixMultiplication {
    
    public static void main(String[] args) {
        MyMatrixClass matrix1 = new MyMatrixClass();
        MyMatrixClass matrix2 = new MyMatrixClass();
        matrix1.setNewMatrix();
        matrix2.setNewMatrix();
        
        matrix1.multiplyMatrix(matrix2);
       
    }
    
}
