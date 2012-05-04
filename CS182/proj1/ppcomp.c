//ppcomp.c

#include "mysorts.h"

int ppcomp(void* x, void* y){
	t_person* a = (t_person*)x;
	t_person* b = (t_person*)y;
	if(x==NULL && y==NULL)
		return 0;
	if(x==NULL)
		return -1;
	if(y==NULL)
		return 1;
		
	if(sscomp(a->surname,b->surname) !=0)
		return sscomp(a->surname,b->surname);
	if(sscomp(a->name,b->name) !=0)
		return sscomp(a->name,b->name);
	return iicomp(&a->age,&b->age);
}
