package utils;

/**
 * Created by hemantkumar on 07/02/19.
 */
public class Timer {
    long startTime;

    public Timer(){
        this.startTime = System.nanoTime();
    }

    public String toString(){
        return String.format("%.8f", (System.nanoTime() - this.startTime)/1000000000.0) + " s";
    }
}
