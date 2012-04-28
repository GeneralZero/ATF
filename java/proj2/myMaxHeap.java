package bridings;

public class myMaxHeap {
    private final int MIN = 15;
    private Object[] theHeap;
    private int size;
    public myMaxHeap(){
        theHeap = new Object[MIN];
        size = 0;
    }

    public myMaxHeap(int cap){
        if(cap<MIN)
            cap=MIN;
        theHeap = new Object[cap];
        size = 0;
    }
    public myMaxHeap(Object[] arr, int s){
        if(arr==null){
            theHeap = new Object[MIN];
            size=0;
        }
        else{
            int i=0;
            theHeap = arr;
            size=s;
            bulidHeap();
             }
        }
    }
    private void bulidHeap(){
        for(int i=(size/2)-1;i>=0;i--)
            shiftDown(i);
    }
    private void shiftDown(int i)
{
    int lc;
    if ((i>= 0) && (i< (size / 2)))
    {
        lc = 2 * i + 1; // left child
        if (((lc + 1) < size) &&(((Comparable)theHeap[lc + 1]).compareTo(theHeap[lc]) > 0))
            lc++; // lc is now largest child insted of left child
        if (((Comparable)theHeap[lc]).compareTo(theHeap[i]) > 0)
        {
            swap(lc, i); 
            shiftDown(lc);
        }
    }
}
    private int shiftUp(int i){
        int p;
        if((i>0)&& (i<size)){
            p=(i-1)/2;
            if((((Comparable)(theHeap[i])).compareTo(theHeap[p]))> 0){
                swap(p,i);
                return shiftUp(p);
            }
        }
        return i;
    }
    public Object removeMax(){
        if(size<=0)
            return null;
        swap(0,--size);
        shiftDown(0);
        return theHeap[size];
    }
    public boolean add(Comparable k){
        if(k==null)
            return false;
        if(size>= theHeap.length){
            Object[] temp = new Object[size*2];
            for(int i=0; i<theHeap.length; i++)
                temp[i] = theHeap[i];
            theHeap=temp;
        }
        theHeap[size] =k;
        shiftUp(size++);
        return true;
    }
    private void swap(int a, int b){
        Object temp = new Object();
        temp = theHeap[b];
        theHeap[b] = theHeap[a];
        theHeap[a] = temp;
    }
    @Override
    public String toString(){
        String temp = "";
        for(int i=0; i<size; i++){
            temp += theHeap[i];
            temp += " \n";
        }
        return temp;

    }
}
