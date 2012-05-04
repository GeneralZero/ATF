//mergeSort.c

#include "mysorts.h"

void mergeSort(void** arr,int n,t_comp comp){
	if((arr!=NULL)&&(n>1)&&(comp!=NULL)){
		void** temp = (void**)malloc(sizeof(void*)*n);
		recMergeSort(arr,n,comp,temp);
		free(temp);
	}
}