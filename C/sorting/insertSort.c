//insertSort.c

#include "mysorts.h"

void insertSort(void** arr,int n,t_comp comp){
	if((arr!=NULL)&&(n>1)&&(comp!=NULL)){
	int i,j;
		for(i=1; i<n; i++)
			for(j=i; (j>0)&&(*comp)(arr[j],arr[j-1])<0; j--)
				swap(arr,j,j-1);
	}
}
