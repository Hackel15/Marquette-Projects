import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.PrintWriter;

/*********************************************************************
 * FileUtils class of static constants and basic file checking routines.
 *
 * Methods:
 * public static Scanner ScannerOpen(String inFileName)
 *
 * Copyright (c) 2011 by Duncan A. Buell. All rights reserved.
 *
 * @author Duncan Buell
 * @version 1.00 2011-07-04
**/
public class FileUtils
{
/*********************************************************************
 * ScannerOpen method to open a file as a Scanner.
 * 
 * The main purpose of this method is to do the error checking in
 * a subordinate method so as not to clutter up the code flow
 * in methods that have to open files.
 * 
 * @param  inFileName the <code>String</code> name of the file to open.
 * @return The opened <code>Scanner</code> known to be not null.
**/
  public static Scanner ScannerOpen(String inFileName)
  {
    Scanner localScanner = null;

    try
    {
      localScanner = new Scanner(new File(inFileName));
    }
    catch (FileNotFoundException ex)
    {
      System.out.println("TAG + ERROR opening inFile " + inFileName);
      System.out.println(ex.getMessage());
      System.out.println("in" + System.getProperty("user.dir"));
      System.out.flush();
      System.exit(1);
    }

    return localScanner;
  } // public static Scanner ScannerOpen(String inFileName)
  
   public static PrintWriter PrintWriterOpen(String outFileName)
  {
    PrintWriter localPrintWriter = null;

//    FileUtils.logFile.printf("%s enter PrintWriterOpen%n",TAG);

    if(outFileName.equals("System.out"))
    {
      localPrintWriter = new PrintWriter(System.out);
    }
    else
    {
      try
      {
        localPrintWriter = new PrintWriter(new File(outFileName));
      }
      catch (FileNotFoundException fileException)
      {
        System.out.println("TAG + ERROR opening inFile " + outFileName);
        System.out.println(fileException.getMessage());
        System.out.println("in" + System.getProperty("user.dir"));
        System.out.flush();
        System.exit(1);
      }
    }
    return localPrintWriter;
  } // public static PrintWriter PrintWriterOpen(String outFileName)

  

} // public class FileUtils
