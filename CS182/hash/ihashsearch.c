//ihashsearch.c

#include "myHash.h"

int ihashsearch(t_ihashtable* ht,int key){
	int home,i,pos;
	if((ht== NULL)||(ht->n<=0))
        	return -1;
     	if((home=ht->h(key))<0)
        	return -1;
	for(pos = home,i=1;(ht->HT[pos]!=EMPTY); i++, pos = (home+ht->p(key,i))%ht->M)
		if(ht->getkey(ht->HT[pos])==key)
			return pos;
	return -1;
}
