import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Killers here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Killers extends Actor
{
     public void act() 
    {
        this.steering();
        this.beingKilled();
    }

    public void steering()
    {
        if(Greenfoot.isKeyDown("down"))
        {
            this.setLocation(this.getX(), this.getY()+5);                 
        }
        if(Greenfoot.isKeyDown("up"))
        {
            this.setLocation(this.getX(), this.getY()-5);                 
        }
        if(Greenfoot.isKeyDown("right"))
        {
            this.setLocation(this.getX()+5, this.getY());                 
        }
        if(Greenfoot.isKeyDown("left"))
        {
            this.setLocation(this.getX()-5, this.getY());                 
        }

    }
    public void beingKilled()

    {
        if(this.isTouching(Balls.class))
        {
            this.setImage("explosion.png");
            Greenfoot.delay(5);
            Greenfoot.playSound("Explosion.wav");
            Greenfoot.playSound("game-over.wav");
            Greenfoot.stop(); 
        }

    }
}
