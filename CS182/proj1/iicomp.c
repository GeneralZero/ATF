//iicomp.c

#include "mysorts.h"

int iicomp(void *x ,void *y){
	int a,b;
        if(x==NULL && y==NULL)
                return 0;
        if(x==NULL)
                return -1;
        if(y==NULL)
                return 1;
	a = *(int *) x;
	b = *(int *) y;
        return a-b;
}

