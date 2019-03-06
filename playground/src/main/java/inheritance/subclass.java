package inheritance;

/**
 * Created by hemantkumar on 10/02/19.
 */
public class subclass implements interfaceA, interfaceB {

    /**
     * This class has an ambiguity, both interfaceA and interfaceB contain the default definition of x(). This will result in compilation error.
     * One can resolve the ambiguity (and satisfy the compiler) by overriding x() in the subclass. One may then explicitly invoke the individual inherited default methods:
     */
    public void x(){
        interfaceA.super.x();
        interfaceB.super.x();
    }
}
