import java.io.File;
import java.io.FileInputStream;
import java.io.FileReader;
import java.util.Scanner;

public class StockTransaction {

	public static void main(String[] args) {

		DList companyNames = new DList();
		Scanner inputStream;
		
		try
		{
			//File fileName = new File("stocks.txt");
			inputStream = new Scanner(new FileReader("C:/Users/jzucca/Desktop/Data Structures/Assignment 4/src/stocks.txt"));
			while (inputStream.hasNextLine())
			{
				String line = inputStream.nextLine();
				int split = line.indexOf(';');
				String abbreviation = line.substring(0, split);
				String title = line.substring(split + 1);
				
				companyNames.addToLast(title, abbreviation);

			}
			
			inputStream = new Scanner(new FileReader("C:/Users/jzucca/Desktop/Data Structures/Assignment 4/src/transactions.txt"));
			while (inputStream.hasNextLine())
			{
				String line = inputStream.nextLine();
				String[] fields = line.split(";");
				
				LLNode company = companyNames.search(fields[0]);
				if(company != null){
					company.getTransactions().addToLast(fields[1], fields[2], fields[3]);
				}
			}
			
		}
		catch (Exception e) 
		{
			System.out.println("Bloop");
			System.out.println(e.getMessage());

		}
		
		Scanner userInput = new Scanner(System.in);
		String input;
		
		do 
		{
			System.out.print("Please enter a input stock quote for realized gain(or loss) for the stock: ");
			input = userInput.nextLine();
			LLNode company = companyNames.search(input);
			if(company != null)
			{
				
			}
			else
			{
				System.out.println("Sorry, the stock quote does not exist in the system.");
			}
			
			
		} while (!input.equals("bloop"));

		

	}

}
