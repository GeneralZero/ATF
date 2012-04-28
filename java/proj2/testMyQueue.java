package bridings;

public class testMyQueue {
    public static void main(String args[]){
        MyPriorityQueue test = new MyPriorityQueue();

        System.out.println(test.toString());

        System.out.println(test.push((Object)(new myBST())));
        System.out.println(test.push((Object)(new myBST())));
        System.out.println(test.push((Object)(new myBST())));
        System.out.println(test.push((Object)(new myBST())));
        System.out.println(test.push((Object)(new myBST())));

        System.out.println(test.getSize());

        System.out.println(test.pop());
        System.out.println(test.pop());
        System.out.println(test.pop());
        System.out.println(test.pop());

        System.out.println(test.toString());
    }
}
