package cgreco;

public class HTable{
	public int size;
	public final int MIN = 10;
	public myMaxHeap[] table; 	

	public HTable(){
		size =MIN;
		table = new myMaxHeap[MIN];
		for(int i=0; i<MIN; i++)
				table[i] = new myMaxHeap(MIN);
	}
	
	public HTable(int tsize){
		size =tsize;
		table = new myMaxHeap[tsize];
		for(int i=0; i<tsize; i++)
				table[i] = new myMaxHeap(MIN);
	}
    
	int key(Person A){
		return  A.Age;
	}
    int probe(int k, int i){
        return k+i;
    }
    int getkey(int k){
        return k%size;
        
    }
    
    public void add(Person A){
		if(A!=null){
			int home, i, newhome;
			home = key(A)%size;
			newhome = home;
			for(newhome = home, i = 0; table[newhome].size>=MIN; i++){
			   newhome = probe(home,i)%size;
			}
			table[newhome].add(A);
		}
    }

    public Person remove(int key){
        int home, i, newhome;
        myMaxHeap A = new myMaxHeap();
        home = getkey(key);
		//System.out.println(table[home].maxObject());
        for(newhome = home, i = 0; table[newhome]!= null && table[newhome].size > 0; i++){
            if(key == key(table[newhome].maxObject())){
				//System.out.println(table[newhome].maxObject());
				A = table[newhome];
				break;
            }
        	newhome= probe(key,i)%size;
		}       
		return A.removeMax();
	}
	
	public Person look(int key){
        int home, i, newhome;
        myMaxHeap A = new myMaxHeap();
        home = getkey(key);
		//System.out.println(table[home].maxObject());
        for(newhome = home, i = 0; table[newhome]!= null && table[newhome].size > 0; i++){
            if(key == key(table[newhome].maxObject())){
				//System.out.println(table[newhome].maxObject());
				A = table[newhome];
				return A.maxObject();
            }
        	newhome= probe(key,i)%size;
		}       
		return null;
	}
}
