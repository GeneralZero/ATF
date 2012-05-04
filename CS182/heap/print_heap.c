//print_heap.c

#include "myheap.h"

void printHeap(t_heap* theHeap){
	int i;
	for(i=0; i<theHeap->current_size;i++)
		printf("%d:%d\n",i,*((int*)theHeap->tree[i]));
	printf("-----------\n");
}
