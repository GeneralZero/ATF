//newMinHeap.c

#include "myheap.h"

t_heap* newHeap(int size){
	t_heap* theHeap;
	theHeap = (t_heap*)malloc(sizeof(t_heap));
	theHeap->tree = (void**)malloc(sizeof(void*)*size);
	theHeap->size_max = size;	
	theHeap->current_size = 0;
	return theHeap;
}
