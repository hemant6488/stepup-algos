package inheritance;

/**
 * Created by hemantkumar on 10/02/19.
 */
public interface interfaceA {
    default void x(){
        System.out.println("In interface A's x().");
    }
}
