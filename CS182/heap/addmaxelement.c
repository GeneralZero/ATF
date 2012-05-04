//addmaxelement.c

#include "myheap.h"

bool addMaxElement(t_heap* theHeap, void* element, t_comph comp){
	if(theHeap==NULL || element == NULL || comp == NULL || theHeap->current_size>=theHeap->size_max)
		return FALSE;
	theHeap->tree[theHeap->current_size] = element;
        shiftMaxUp(theHeap, theHeap->current_size++, comp);
        return TRUE;
}
