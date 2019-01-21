import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class MyWorld here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class MyWorld extends World
{

    /**
     * Constructor for objects of class MyWorld.
     * 
     */
    public MyWorld()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(600, 400, 1); 
        prepare();
    }

    /**
     * Prepare the world for the start of the program.
     * That is: create the initial objects and add them to the world.
     */
    private void prepare()
    {
        Killers killers = new Killers();
        addObject(killers,108,215);
    }
     public void act()
    {
      if(Greenfoot.getRandomNumber(100) < 5)
      {
        
        
      int posX = Greenfoot.getRandomNumber(100)+500;  
      int posY = Greenfoot.getRandomNumber(350);
      this.addObject(new Balls(), posX, posY);
    }
    }
    
}
