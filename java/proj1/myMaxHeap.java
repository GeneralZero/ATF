package cgreco;

public class myMaxHeap {
    private final int MIN = 15;
    private Person[] theHeap;
    public int size;
    public myMaxHeap(){
        theHeap = new Person[MIN];
        size = 0;
    }

    public myMaxHeap(int cap){
        theHeap = new Person[cap];
        size = 0;
    }
    public myMaxHeap(Person[] arr, int s){
        if(arr==null){
            theHeap = new Person[MIN];
            size=0;
        }
        else{
            theHeap = arr;
            size=s;
            bulidHeap();
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
        if (((lc + 1) < size) &&(theHeap[lc + 1].TBLevel -theHeap[lc].TBLevel > 0))
            lc++; // lc is now largest child insted of left child
        if (theHeap[lc].TBLevel - theHeap[i].TBLevel > 0)
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
            if(theHeap[i].TBLevel - theHeap[p].TBLevel > 0){
                swap(p,i);
                return shiftUp(p);
            }
        }
        return i;
    }
    public Person removeMax(){
        if(size<=0)
            return null;
        swap(0,--size);
        shiftDown(0);
        return theHeap[size];
    }
    public boolean add(Person k){
        if(k==null)
            return false;
        theHeap[size] = k;
        shiftUp(size++);
        return true;
    }

	public Person maxObject(){
		return theHeap[0];
	}

    private void swap(int a, int b){
        Person temp = new Person();
        temp = theHeap[b];
        theHeap[b] = theHeap[a];
        theHeap[a] = temp;
    }
	
	public void print(){
		for(int i=0; i<size; i++)
			System.out.println(theHeap[i]);
	}
}
