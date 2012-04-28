package bridings;

public class testMin {
    public static void main(String args[]){
        myMinHeap test = new myMinHeap(10);

        String s = "11010110101010"+'\u0000';
        System.out.println( s.substring(1));
        System.out.println(rec(s));
        System.out.println("DONE");
        test.add('a');
        test.add('c');
        test.add('f');
        test.add('q');
        test.add('w');
        System.out.println("DONE");
        System.out.println(test.toString());
        System.out.println("DONE");
        test.removeMin();
        System.out.println(test.toString());
        test.removeMin();
        System.out.println(test.toString());
        test.removeMin();
        System.out.println(test.toString());
        test.removeMin();
        System.out.println("DONE");
        System.out.println(test.toString());
        System.out.println("DONE");
    }
    private static String rec(String a){
         String ret=a;
         while(ret.substring(1).equalsIgnoreCase("\u0000")){
            if(ret.charAt(0)=='0'){
                ret = ret.substring(1);
                rec(ret);
            }
            else if (ret.charAt(0) == '1'){
                ret = ret.substring(1);
                rec(ret);
            }
            else{
                System.out.println("String too short");
            }
        }
        return (ret);
    }
}
