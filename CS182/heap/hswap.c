//hswap.c

#include "myheap.h"

void hswap(t_heap* theHeap, int a, int b){
	void* temp;
	temp = (void*)malloc(sizeof(void));
	temp = theHeap->tree[b];
	theHeap->tree[b] = theHeap->tree[a];
	theHeap->tree[a] = temp;
	free(temp);
}
