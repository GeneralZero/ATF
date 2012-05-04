//shiftMinDown.c

#include "myheap.h"

void shiftMinDown(t_heap* theHeap, int index, t_comph comp){
	int lc;
	if(index>=0&&theHeap!=NULL&&comp!=NULL&& 2*index+1 < theHeap->current_size){
		lc = 2 * index + 1;
		if((lc+1<theHeap->current_size)&&((*comp)(theHeap->tree[lc + 1],theHeap->tree[lc])<0))
			lc++;
		if(((*comp)(theHeap->tree[lc],theHeap->tree[index])<0)){
		    swap(theHeap,lc,index);
		    shiftMinDown(theHeap,lc,comp);
		}
	}
}
