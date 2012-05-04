//radixSort.c

#include "mysorts.h"

void radixSort(int* arr, int n, int radix){
	if((arr!=NULL)&&(n>1)&&(radix>1)){
		int i;
		int max;
		int exp;
		int* temp = (int*)malloc(sizeof(int)*n);
		int* count = (int*)malloc(sizeof(int)*radix);
		for(max = arr[0],i=0;i<n;i++)
			if(arr[i]>max)
				max=arr[i];
		for(exp=1; exp<=max; exp*=radix){
			for(i=0; i<radix; i++)
				count[i]=0;
			for(i=0; i<n; i++)
				count[(arr[i]/exp)%radix]++;
			for(i=1; i<radix; i++)
				count[i]+=count[i-1];
			for(i=n-1; i>=0; i--)
				temp[--count[(arr[i]/exp)%radix]] = arr[i];
			for(i=0; i<n; i++)
				arr[i]=temp[i];
		}
		free(temp);
		free(count);
	}
}