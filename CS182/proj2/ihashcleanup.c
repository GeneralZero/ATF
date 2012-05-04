//ihashcleanup.c

# include "myHash.h"

void  ihashcleanup(t_ihashtable *ht){
     void  **temp;
     void **arr;
     int i;
     temp = (void**)malloc(sizeof(void*)*ht->M);
     if(ht!=NULL){
          arr = (void**)malloc(sizeof(void*)*ht->M);
          for(i=0; i<ht->M; i++)
               arr[i] = EMPTY;
          temp = ht->HT;
          ht->HT = arr;
          ht->n=0;
          for(i=0;i<ht->M; i++)
               if(temp[i]!=TOMB&&temp[i]!=EMPTY)
                    ihashadd(ht,temp[i]);
          }
     free(temp);
     free(arr);
}