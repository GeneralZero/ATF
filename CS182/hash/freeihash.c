//freeihash.c

#include "myHash.h"

void freeihash(t_ihashtable ** ht){
	free((*ht));
	free((*ht)->HT);
}
	
