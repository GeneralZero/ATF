//addminelement.c

#include "myheap.h"

bool addMinElement(t_heap* theHeap, void* element, t_comph comp){
	if(theHeap==NULL || element == NULL || comp == NULL || theHeap->current_size>=theHeap->size_max)
		return FALSE;
	theHeap->tree[theHeap->current_size] = element;
        shiftMinUp(theHeap, theHeap->current_size++, comp);
        return TRUE;
}
