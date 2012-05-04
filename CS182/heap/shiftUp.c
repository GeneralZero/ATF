//shiftMinUp.c

#include "myheap.h"

void shiftMinUp(t_heap* theHeap, int index, t_comph comp){
	if(index>0&&theHeap!=NULL&&comp!=NULL){
		int p;
		p = (index-1)/2;
		if((*comp)(theHeap->tree[index],theHeap->tree[p])<0){
		        swap(theHeap,p,index);
		        shiftUp(theHeap,p,comp);
		}
	}
}

