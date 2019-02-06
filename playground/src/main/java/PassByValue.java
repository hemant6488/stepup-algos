/**
 * Created by hemantkumar on 05/02/19.
 */

class Example{
    public Example(String s){
        this.x = s;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }

    String x;

}
public class PassByValue {
    public static void main(String args[]){
        Example e1 = new Example("A");
        Example e2 = new Example("B");

        System.out.println(e1.getX());
        System.out.println(e2.getX());

        processExamples(e1, e2);

        System.out.println(e1.getX());
        System.out.println(e2.getX());
    }

    private static void processExamples(Example e1, Example e2) {
        e1.setX("C");
        e2 = new Example("D");

        System.out.println(e1.getX());
        System.out.println(e2.getX());
    }
}
