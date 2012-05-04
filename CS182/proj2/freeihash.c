//freeihash.c

#include "myHash.h"

void freeihash(t_ihashtable ** ht){
	free((*ht)->HT);	
	free((*ht));	
}
	
