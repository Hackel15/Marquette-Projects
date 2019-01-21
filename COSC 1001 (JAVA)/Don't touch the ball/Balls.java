import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Balls here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Balls extends Actor
{

    public Balls ()
    {
        int red = Greenfoot.getRandomNumber(256);   
        int green = Greenfoot.getRandomNumber(256);
        int blue = Greenfoot.getRandomNumber(256);

        GreenfootImage image = new GreenfootImage (50,50);
        Color color = new Color(red, green, blue);
        this.setImage(image);
        this.getImage().setColor(color);
        this.getImage().drawOval(0, 0, 50, 50);
        this.getImage().fillOval(0, 0, 50, 50);

    }

    public void turningAround()
    {
        if(this.isAtEdge())
        {
            this.turn(Greenfoot.getRandomNumber(90)+90);  

        }

    }

    public void act() 
    {
        this.move(2);
        this.turningAround();
        this.killingEachOthers();
    } 

    public void killingEachOthers()
    {
        if(this.isTouching(Balls.class))
        {
            this.removeTouching(Balls.class);   

        }

    }

    
}
