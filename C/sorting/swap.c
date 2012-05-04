//swap.c

#include "mysorts.h"

void swap(void** arr, int x, int y){
	void* temp = (void*)malloc(sizeof(void));
	temp = arr[x];
	arr[x] = arr[y];
	arr[y] = temp;
}