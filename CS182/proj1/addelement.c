//addelement.c

#include "myheap.h"

bool addelement(t_heap theHeap, void* element, t_comp comp){
	if(theHeap==NULL || element == NULL || comp == NULL || theHeap->current_size<=theHeap->size_max)
		return False
	theHeap->tree[theHeap->current_size] = element;
        shiftDown(theHeap, theHeap->current_size++, comp);
        return true;
}
