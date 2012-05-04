//sscomp.c

#include "mysorts.h"

int sscomp(void* x ,void* y){
	if(x==NULL && y==NULL)
		return 0;
	if(x==NULL)
		return -1;
	if(y==NULL)
		return 1;
	return strcmp((char*)x,(char*)y);
	}