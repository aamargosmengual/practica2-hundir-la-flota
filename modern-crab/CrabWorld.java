import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class CrabWorld here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class CrabWorld extends World
{

    /**
     * Constructor for objects of class CrabWorld.
     * 
     */
    public CrabWorld()
    {    
        super(560, 560, 1); 
        prepare();
    }
    
    /**
     * Prepare the world for the start of the program.
     * That is: create the initial objects and add them to the world.
     */
    private void prepare()
    {
        Crab crab = new Crab();
        addObject(crab,251,227);
        Worm worm = new Worm();
        addObject(worm,438,153);
        Worm worm2 = new Worm();
        addObject(worm2,465,444);
        Worm worm3 = new Worm();
        addObject(worm3,154,383);
        Worm worm4 = new Worm();
        addObject(worm4,84,50);
        Lobster lobster = new Lobster();
        addObject(lobster,52,476);
        Counter counter = new Counter();
        addObject(counter,523,33);
    }
}
