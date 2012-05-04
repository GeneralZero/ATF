//new_ihashtable.c

#include "myHash.h"

t_ihashtable *new_ihashtable(int cap, t_ikey key, t_ihash hash, t_iprobe probe){
	t_ihashtable *new;
	if((key!=NULL)&&(hash!=NULL)&&(probe!=NULL)){
		if(cap<MIN)
			cap = MIN;
		new = (t_ihashtable*)malloc(sizeof(t_ihashtable));
		new->HT = (void**)malloc(sizeof(void*)*cap);
		new->M = cap;
		new->n = 0;
		new->h = hash;
		new->p = probe;
		new->getkey = key;
	}
	
	return new;
 }
