//test.c

#include "myheap.h"

int main(int argc, char **argv){
	int i =55, j = 51, k = 8,p = 99,o=42 ;
	t_heap* theHeap = newHeap(10);
	addMaxElement(theHeap, (void*)&i, &iicomp);
	addMaxElement(theHeap, (void*)&j, &iicomp);	
	addMaxElement(theHeap, (void*)&k, &iicomp);
	addMaxElement(theHeap, (void*)&p, &iicomp);
	printHeap(theHeap);
	printf("%d\n",*((int*)popMaxHeap(theHeap, &iicomp)));
	printHeap(theHeap);
	addMaxElement(theHeap, (void*)&o, &iicomp);
	addMaxElement(theHeap, (void*)&k, &iicomp);
	printf("%d\n",*((int*)popMaxHeap(theHeap, &iicomp)));
	freeHeap(theHeap);
}
