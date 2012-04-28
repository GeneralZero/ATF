package bridings;

import java.util.Scanner;

class BSTNode implements Comparable{
    public char letter;
    public int prioity;
    public BSTNode lc;
    public BSTNode rc;
    public BSTNode(char l, int p){
        this.letter = l;
        this.prioity =p;
    }
    public BSTNode(BSTNode l, BSTNode r){
        this.letter = '\u0000';
        this.prioity = l.prioity + r.prioity;
        this.lc = l;
        this.rc = r;
    }
    public void Strings(String ret){
            if (this.lc != null)
                    this.lc.Strings(ret + '0');
            if (this.rc != null)
                    this.rc.Strings(ret + '1');
            if(this.rc==null && this.rc==null)
                System.out.println("Binary Value: " + ret + "\tCharacter: " +letter + "\tFrequency" + prioity);
    }
    public int compareTo(Object o){
        return this.prioity - ((BSTNode) o).prioity;
    }
}

public class MyHuffmanProcessor {
    private static MyPriorityQueue Queue;

    final static int ASCII = 256;

    public static void main(String args[]){
        short i= -1;
        
        while(i!=0){
            i = showMenu();
            Scanner cin = new Scanner(System.in);
            if(i == 1){
                System.out.println("Type a string encode as a Hoffman tree:\n");
                bulidTree(cin.nextLine().toCharArray());
            }
            if(i == 2){
                System.out.println("Type a Binary string to decode:\n");
                System.out.println(binString(cin.nextLine().toCharArray()));
            }
            if(i == 3)
                printTree();
       }
    }

    private static void bulidTree(char[] input){
        int[] freq = new int[ASCII];
        MyPriorityQueue theQueue = new MyPriorityQueue(input.length);
        for(int i=0; i<input.length; i++){
            if(input[i] != '\u0000')
                freq[i]++;
            for(int j=i+1; j<input.length; j++){
                if(input[i] == input[j] && input[i] != '\u0000'){
                    freq[i]++;
                    input[j]='\u0000';
                }
            }
        }

        for(int i=0; i<freq.length; i++){
            if(freq[i]> 0){
                theQueue.push((Object)(new BSTNode(input[i],freq[i])));
            }
        }

        while(theQueue.getSize()>1)
            theQueue.push((Object)(new BSTNode((BSTNode)theQueue.pop(),(BSTNode)theQueue.pop())));
        Queue = theQueue;
        System.out.println("The String has Been comperessed");
    }

    private static short showMenu(){
        Scanner cin = new Scanner(System.in);
        short i = 5;
        String str = "";
        while(i<0 || i > 4){
            System.out.println("\n1) Build Tree From String "
                    + "\n2) Enter string in binary"
                    + "\n3) View Tree"
                    + "\n0) Exit");
            str = cin.next();
            if(Character.isDigit(str.charAt(0))){
                if(str.length()<2)
                    i= Short.parseShort(str.trim());
            }
        }
        return i;
    }

    private static String binString(char[] input){
        String ret= "";
        if(Queue==null || Queue.front()==null)
            return "The object is not defined yet.";
        for(int i=0; i<(input.length); i++){
            if(!(input[i]== '0' || input[i]== '1'))
                return "Not a valid String.";
        }
        return stringRec(new String(input),(BSTNode)(Queue.front()));
    }

    public static void printTree(){
         if(Queue!=null){
			if(Queue.front()!=null){
				System.out.print("(");
				inOrder((BSTNode)(Queue.front()));
				System.out.print(")");
			}
			else
				System.out.println("The object is not defined yet.");
        }
        else
            System.out.println("The object is not defined yet.");
    }
    private static void inOrder(BSTNode root){
            if(root.lc != null){
                System.out.print("(");
                inOrder(root.lc);
                System.out.print(")");
            }
            if(root.lc == null && root.rc == null && root.letter != ' ')
                System.out.print("(" + root.letter + "-" + root.prioity + ")");
            if(root.lc != null && root.rc != null)
                System.out.print(" " + root.prioity + " ");
            if(root.rc != null){
                System.out.print("(");
                inOrder(root.rc);
                System.out.print(")");
        }
    }
    private static String stringRec(String str, BSTNode root){
        BSTNode node = root;
        String ret="";
        for(int i=0; i< str.length(); i++){
            if(node.lc == null && node.lc == null){
                ret += (node.letter);
                node = root;
            }
            else{
                if(str.charAt(i)=='0'){
                    node = node.lc;
                }
                if (str.charAt(i) == '1'){
                    node = node.rc;
                }
            }
        }
        return ret;
    }
}
