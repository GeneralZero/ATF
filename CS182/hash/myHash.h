#ifndef _MYHASH_H_
#define _MYHASH_H_

#include <stdlib.h>

typedef int (*t_ikey)(void*);
typedef int (*t_ihash)(int);
typedef int (*t_iprobe)(int,int);

#ifndef TOMB
#define TOMB (void*)1
#endif

#ifndef MIN
#define MIN 10
#endif

#ifndef EMPTY
#define EMPTY (void*)0
#endif

#ifndef NULL
#define NULL 0
#endif

typedef struct	s_ihashtable
{
  void**	HT; // The table
  int		M; // Max capacity of HT
  int		n; // number of elements currently in HT
  t_ikey	getkey; // function to get a key from a void*
  t_ihash     	h; // hash function, takes an int
  t_iprobe	p;
}		t_ihashtable;

t_ihashtable	*new_ihashtable(int cap,t_ikey,t_ihash,t_iprobe); //allocates everything
int       ihashadd(t_ihashtable*,void* elem); //adds an elem to the HT
void     *ihashremove(t_ihashtable*,int key); //remove items with key
int       ihashsearch(t_ihashtable*,int key); //returns item with key
void     freeihash(t_ihashtable **); //free the HT and structure
void     ihashcleanup(t_ihashtable*); //"cleans up the hash table" by
// getting rid of tombstones and replacing all items in their ideal place
#endif

