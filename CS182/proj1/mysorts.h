#ifndef _MYSORTS_H_
#define _MYSORTS_H_

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#ifndef NULL
#define NULL 0
#endif

typedef struct	s_person
{
  char		*name;
  char		*surname;
  int		age;
}		t_person;

typedef int (*t_comp)(void*, void*);
typedef char boolean;

// Program all 4 of these
int ppcomp(void*, void*); // compares 2 t_person* using surname, then name, then age (older person first)
int sscomp(void*, void*); // compares 2 char*
int iicomp(void*, void*); // compares 2 ints (though you will receive a pointer to each int, not the ints themselves)
int cccomp(void*, void*); // compares 2 characters (though will receive pointers to those chars, not the chars themselves)

// Program at least 1 of these 3 easy sorting algorithms
void insertSort(void**, int, t_comp);

// Program at least 1 of these 2 "fun" sorting algorithms
void radixSort(int*, int, int); // (int array, size of array, base used)

// And finally at least 1 of these 2 recursive sorting algorithms
void mergeSort(void**, int, t_comp);

// You may need these. Feel free to write them as you see fit. Not necessarily with the signature given.

void recmergeSort(void**, int, int, void**, t_comp); // used by mergeSort, the second void** is your temporary array, allocated by mergeSort.
void swap(void**, int, int); 

#endif


