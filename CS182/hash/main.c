#include <stdio.h>
#include "myHash.h"


int	pigetkey(void *p)
{
  if (p == NULL)
    return -1;
  return (*((int*)p));
}

int	inthash(int k)
{
  if (k < 0)
    return -1;
  return k % 16;
}

int	probe(int k, int i)
{
  if (k < 0 || i < 0)
    return -1;
  if (i == 0)
    return 0;
  return 3 * i;
}

int	main(int argc, char **argv)
{
  int	arr[argc - 1];
  int	i;
  t_ihashtable *H;
  int n = 15;

  for (i = 1; i < argc; i++)
    arr[i - 1] = atoi(argv[i]);
  for (i = 0; i < argc - 1; i++)
    printf("%d ", arr[i]);
  printf("\n");
  H = new_ihashtable(20, &pigetkey, &inthash, &probe);
  for (i = 0; i < argc - 1; i++)
	ihashadd(H, &arr[i]);
  ihashremove(H, 23);
  //ihashremove(H, 655);
  printf("%d ",*((int*)ihashremove(H, 655)));
  printf("%d ",*((int*)ihashremove(H, 25)));
  ihashadd(H, &n);
  for (i = 0; i < 20; i++)
    {
      printf("%d:", i);
      if (H->HT[i] == EMPTY)
	printf("EMPTY\n");
      else if (H->HT[i] == TOMB)
	printf("TOMB\n");
      else
	printf("%d\n", *((int*)(H->HT[i])));
    }
  printf("===========\n");
  ihashcleanup(H);

  for (i = 0; i < 20; i++)
    {
      printf("%d:", i);
      if (H->HT[i] == EMPTY)
	printf("EMPTY\n");
      else if (H->HT[i] == TOMB)
	printf("TOMB\n");
      else
	printf("%d\n", *((int*)(H->HT[i])));
    }
  printf("===========\n");

  freeihash(&H);
  return 1;
}
