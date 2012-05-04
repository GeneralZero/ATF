// my.h

#ifndef _MY_H_
#define _MY_H_
#ifndef NULL
#define NULL ((void*)0)
#endif

#include <ctype.h>
//int write(int, const void*, int);
void free(void*);


void my_char(char);
void my_str(char*);
void my_int(int);
void my_num_base(int, char*);
char*my_num_base2(int, char*);

void my_alpha();
void my_digits();
char* my_digits2();

int my_find(char*, char);
int my_rfind(char*, char);

int my_strlen(char*);
int my_revstr(char*);

//PROJECT 2

//void	*malloc(int);
//void* malloc(size_t);

void	exit(int);

char*	my_strcat(char*,char*);
int		my_strcmp(char*, char*);
int		my_strncmp(char*, char*, int);
char*	my_strconcat(char*,char*);
char*	my_strnconcat(char*, char*, int);
char*	my_stdstrnconcat(char*, char*, int);
char*	my_strcpy(char*, char*);
char*	my_strncpy(char*, char*, int);
char*	my_strdup(char*);
char*	my_strindex(char*, char);
char*	my_strnindex(char*, char, int);
void*	my_xmalloc(int);

// Project 3
char*	 my_vect2str(char**);
char**	 my_str2vect(char*);

//Project 4
int my_atoi(char*);
#endif
