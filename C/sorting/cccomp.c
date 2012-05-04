//cccomp.c

#include "mysorts.h"

int cccomp(void *x ,void *y){
	if(x==NULL && y==NULL)
		return 0;
	if(x==NULL)
		return -1;
	if(y==NULL)
		return 1;
	return *((char*)x) - *((char*)y);
}
