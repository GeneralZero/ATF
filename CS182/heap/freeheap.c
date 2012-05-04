//freeHeap.c

#include "myheap.h"

bool freeHeap(t_heap* h){
	free(h->tree);
	free(h);
	return TRUE;
}

