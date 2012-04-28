package bridings;

public class testBST{
    public static void main(String args[]){
        myBST test = new myBST();

        System.out.println(test.toString());

        System.out.println(test.add(56));
        System.out.println(test.add(6));
        System.out.println(test.add(5));
        System.out.println(test.add(20));
        System.out.println(test.add(42));

        System.out.println(test.toString());

        System.out.println(test.find(56));
        System.out.println(test.find(42));
        System.out.println(test.find(1));
        System.out.println(test.find(0));

        System.out.println(test.remove(56));
        System.out.println(test.remove(6));
        System.out.println(test.remove(5));
        System.out.println(test.remove(42));

        System.out.println(test.toString());
    }
}
