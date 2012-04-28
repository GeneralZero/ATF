package bridings;

public class testMax {
    public static void main(String args[]){
        myMaxHeap test = new myMaxHeap(10);

        System.out.println(test.toString());
        System.out.println("DONE");
        test.add('a');
        test.add('c');
        test.add('f');
        test.add('q');
        test.add('w');
        System.out.println("DONE");
        System.out.println(test.toString());
        System.out.println("DONE");
        test.removeMax();
        System.out.println(test.toString());
        test.removeMax();
        System.out.println(test.toString());
        test.removeMax();
        System.out.println(test.toString());
        test.removeMax();
        System.out.println("DONE");
        System.out.println(test.toString());
        System.out.println("DONE");
    }
}
