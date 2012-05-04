//popMinHeap.c

#include "myheap.h"

void* popMinHeap(t_heap* theHeap, t_comph comp){
	if(theHeap==NULL||comp==NULL||theHeap->current_size<=0)
		return NULL;
	swap(theHeap,0,--(theHeap->current_size));
	shiftMinDown(theHeap, 0, comp);
	return theHeap->tree[theHeap->current_size];
}
