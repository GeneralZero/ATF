//lookHeap.c

#include "myheap.h"

void* lookHeap(t_heap* theHeap){
	if(theHeap==NULL||theHeap->current_size<=0)
		return NULL;
	return theHeap->tree[0];
}
