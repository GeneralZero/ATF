#include "mysorts.h"

int main(int argc, char** argv)
{
  int i;
  int usort[] = {77,58,50,34,82,92,31,17,93,41,41,12,92,8};
  char* fname[]= {"bob","man","moo","mike","zach","dave","doc","angela","jeff","mike","doctor","brian","jethro","audith"};
  char* lname[]= {"bulider","mr","cow","arpia","shultz","haughee","lib","lopicclo","eteal","cahil","librian","ridings","petnami","summauach"};
  t_person** arr = (t_person**)malloc(sizeof(t_person*)*3);
  
  char** uchar = (char**)malloc(sizeof(char*)*5);
  
  char a = 's';
  char b = 'e';
  char c = 'r';
  char d = 'y';
  char e = 'h';
  
  uchar[0] = &a;
  uchar[1] = &b;
  uchar[2] = &c;
  uchar[3] = &d;
  uchar[4] = &e;
  
	/*  
	t_person* a = (t_person*)malloc(sizeof(t_person));
	t_person* b = (t_person*)malloc(sizeof(t_person));
	t_person* c = (t_person*)malloc(sizeof(t_person));
	
	a->name = "bob";
	a->surname = "thebulider";
	a->age = 18;
	b->name = "bob";
	b->surname = "thebulider";
	b->age = 21;
	c->name = "adam";
	c->surname = "man";
	c->age = 20;
	
      arr[0] = a;
	  arr[1] = b;
	  arr[2] = c;
	
	for (i = 0; i < 3; i++)
    {
      printf("%d ", arr[i]->age);
	  printf("%s ", arr[i]->name);
	  printf("%s ", arr[i]->surname); 
	  printf("\n");
    }
	 printf("\n");*/
  //insertSort((void**)(&argv[1]),argc - 1, &ppcomp);
  insertSort((void**)uchar, 5, &cccomp);
  //mergeSort((void**)fname,14, &sscomp);
  
  	for (i = 0; i < 5; i++)
    {
	  printf("%c ", *uchar[i]); 
	  printf("\n");
    }

  return 0;
}
