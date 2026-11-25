import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Un contador que muestra un texto con un número en pantalla.
 */
public class Counter extends Actor
{
    private static final Color transparent = new Color(0, 0, 0, 0);
    private int score = 0;
    private int target;
    private String text;
    private int stringLength;

    public Counter()
    {
        this("Score: ");
    }

    public Counter(String prefix)
    {
        text = prefix;
        stringLength = (text.length() + 2) * 10;
        setImage(new GreenfootImage(stringLength, 24));
        updateImage();
    }

    public void add(int score)
    {
        this.score += score;
        updateImage();
    }

    public void subtract(int score)
    {
        this.score -= score;
        updateImage();
    }

    public int getValue()
    {
        return score;
    }

    public void setValue(int newValue)
    {
        score = newValue;
        updateImage();
    }

    private void updateImage()
    {
        GreenfootImage image = getImage();
        image.clear();
        image.setColor(Color.BLACK);
        image.drawString(text + score, 1, 18);
    }
}