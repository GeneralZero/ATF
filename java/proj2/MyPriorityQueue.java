package bridings;

public class MyPriorityQueue {
        private myMinHeap theHeap;
        private int size;
    
    public MyPriorityQueue(){
        theHeap = null;
    }
    public MyPriorityQueue(int s){
        theHeap = new myMinHeap(s);
    }

    public MyPriorityQueue(Comparable[] arr, int s){
        theHeap = new myMinHeap(arr, s);
    }

    public boolean push(Object a){
        if(a != null && size < theHeap.getLength()){
            theHeap.add((Comparable)a);
            size++;
            return true;
        }
        return false;
    }

    public Object pop(){
        if(size!=0){
            size--;
            return theHeap.removeMin();
        }
        return null;
    }

    public Object front(){
        Object temp =  theHeap.removeMin();
        theHeap.add((Comparable)temp);
        return temp;
    }
    public int getSize(){
        return theHeap.getSize();
    }
    public boolean isEmpty(){
        return (this.getSize() ==0);
    }

}
