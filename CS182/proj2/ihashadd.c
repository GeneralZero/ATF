//ihashadd(t_ihashtable *ht)

#include "myHash.h"

int ihashadd(t_ihashtable *ht, void* elem){
     int home,i,k,pos;
     if((ht== NULL)||(elem==NULL)||(ht->n>=ht->M))
          return -1;
     if((k=ht->getkey(elem))<0)
          return -1;
     home = ht->h(k)%ht->M;
     for(pos = home,i=1;(ht->HT[pos]!=EMPTY)&&(ht->HT[pos]!=TOMB); i++,pos = (home + ht->p(k,i))%(ht->M))
		if( *((int*)elem) == *((int*)(ht->HT[pos])) )
			return -1;
     ht->HT[pos] = elem;
     ht->n++;
     return pos;
}
