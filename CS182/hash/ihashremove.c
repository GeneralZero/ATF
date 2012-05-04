//ihashremove.c

#include "myHash.h"

void* ihashremove(t_ihashtable *ht, int k){
     int home,i,j,pos;
     void* ret;
     ret = (void*)malloc(sizeof(void));
     if((ht!=NULL)&&(ht->n>0)&&(k>=0)){
          home = ht->h(k)%ht->M;
          for(pos = home,i=1; ht->HT[pos]!=EMPTY;i++)
               if((ht->HT[pos]!=TOMB)&&(k==ht->getkey(ht->HT[pos]))){
                    ret = ht->HT[pos];
                    ht->HT[pos] = TOMB;
                    break;
               }
          //pos = (pos ==home);
          return ret;
     }
     return (void*)-1;
 }
