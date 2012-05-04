//eecomp.c

#include "mygraph.h"

int eecomp(void *x ,void *y){
	int a,b;
        if(x==NULL && y==NULL)
                return 0;
        if(x==NULL)
                return -1;
        if(y==NULL)
                return 1;
	a = ((t_edge*)x)->weight;
	b = ((t_edge*)y)->weight;
        return a-b;
}
