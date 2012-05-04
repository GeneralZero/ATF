#ifndef _MYHEAP_H_
#define _MYHEAP_H_

#include <stdlib.h>
#include <stdio.h>

#ifndef NULL
#define NULL 0
#endif

#ifndef TRUE
#define TRUE 1
#endif

#ifndef FALSE
#define FALSE 0
#endif

typedef char bool;

typedef struct s_heap
{
	int		size_max;
	int		current_size;
	void**	tree;
}t_heap;

typedef int (*t_comph)(void*, void*);
int iicomp(void*, void*);

t_heap* newHeap(int size);//creates a new heap
bool freeHeap(t_heap*);//frees a heap

void* popMinHeap(t_heap* theHeap, t_comph);// Remove the max value from the top of the Queue
bool addMinElement(t_heap* theHeap, void* element, t_comph);// add the value to the Queue
bool addMaxElement(t_heap* theHeap, void* element, t_comph);
void hswap(t_heap* theHeap, int a, int b);// swap two indexices in the Heap
void shiftMinDown(t_heap* theHeap, int index, t_comph);// Shift an index down
void shiftMinUp(t_heap* theHeap, int index, t_comph);//shift an index up
void shiftMaxDown(t_heap* theHeap, int index, t_comph);
void shiftMaxUp(t_heap* theHeap, int index, t_comph);
void printHeap(t_heap* theHeap);
bool freeHeap(t_heap* h);
void* lookHeap(t_heap* theHeap);

#endif
