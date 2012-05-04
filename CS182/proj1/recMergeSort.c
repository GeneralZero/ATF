//recMergeSort.c

#include "mysorts.h"

void recMergeSort(void** arr, int n,t_comp comp,void** temp){
	int m,i,j,k;
	if((arr!=NULL)&&(comp!=NULL)&&(n>1)&&(temp!=NULL)){
			m=n/2;
			recMergeSort(arr,m,comp,temp);
			recMergeSort(&arr[m],n-m,comp,&temp[m]);
			for(i=0;i<m;i++)
				temp[i] = arr[i];
			for(j=n-1;i<n;i++,j--)
				temp[j] = arr[i];
			for(i=0,j=n-1,k=0;k<n;k++){
				if((*comp)(temp[i],temp[j])<=0)
					arr[k]=temp[i++];
				else
					arr[k]=temp[j--];
			}
	}
}