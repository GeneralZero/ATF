//main.c

#include "../lib/my.h"

int main(int argc, char** argv)
{
	//Project 2
	/*
	char* test1;
	test1 =(char*)my_xmalloc(50*sizeof(char));
	my_strcat(test1, "Hello1");
	my_str(test1);
	my_char('\n');
	
	char* test2;
	test2 =(char*)my_xmalloc(50*sizeof(char));
	my_strcat(test2, "Hello World");
	my_str(test2);
	my_char('\n');

	my_str(my_strcat(test1, test2));//Hello1Hello World
	my_char('\n');
	my_str(my_strcat(test1, "Test"));//HelloTest
	my_char('\n');
	my_str(my_strcat(test1, ""));//Hello1
	my_char('\n');
	my_str(my_strcat(test1, NULL));//Hello1
	my_char('\n');
	my_str(my_strcat(NULL, NULL));//NULL
	my_char('\n');
	my_str(my_strcat(NULL, test1));//NULL
	my_char('\n');

	my_str(my_strconcat(test1, test2)); //Hello1Hello World
	my_char('\n');
	my_str(my_strconcat(NULL, test2));//Hello World
	my_char('\n');
	my_str(my_strconcat(test1, NULL));//Hello1
	my_char('\n');
	my_str(my_strconcat(NULL, NULL));//NULL
	my_char('\n');
	
	
	my_str(my_strnconcat(test1, test2 ,10)); //Hello
	my_char('\n');
	my_str(my_strnconcat(NULL, test2 ,5)); //Hello World Error
	my_char('\n');
	my_str(my_strnconcat(test1, NULL ,5));//Hello1 Error
	my_char('\n');
	
	my_str(my_stdstrnconcat(test1, test2, 3));//Hel
	my_char('\n');
	my_str(my_stdstrnconcat(NULL, test2, 3));//Hel
	my_char('\n');
	my_str(my_stdstrnconcat(test1, NULL, 89));//NULL
	my_char('\n');
	my_str(my_stdstrnconcat(test1, NULL, 3));//Hel
	my_char('\n');
	my_str(my_stdstrnconcat(NULL, NULL, 3));//NULL
	my_char('\n');

	my_int(my_strcmp(test1, test2));//17
	my_char('\n');
	my_int(my_strcmp(test1, NULL));//1
	my_char('\n');
	my_int(my_strcmp(NULL, test2));//-1
	my_char('\n');
	
	my_int(my_strncmp(test1, test2,4));//0
	my_char('\n');
	my_int(my_strncmp(NULL, test2,9));//-1
	my_char('\n');
	my_int(my_strncmp(test1, NULL,9));//1
	my_char('\n');
	
	my_str(my_strcpy(test1, test2));//Hello World
	my_char('\n');
	my_str(my_strcpy(NULL, test2));//NULL
	my_char('\n');
	my_str(my_strcpy(test1, NULL));//Hello1
	my_char('\n');
	
	my_str(my_strncpy(test1, test2,9));//Hello Wor
	my_char('\n');
	//my_str(my_strncpy(NULL, test2,9));//NULL	
	my_str(my_strncpy(NULL, test2,4));//NULL
	my_char('\n');
	//my_str(my_strncpy(test1, NULL,9));//Hello1
	my_str(my_strncpy(test1, NULL,3));//Hello1 Error
	my_char('\n');
	my_char('\n');
	my_str(my_strindex(test1, 'l'));//NULL
	my_char('\n');
	my_str(my_strindex(NULL, 'l'));//Hello1
	my_char('\n');
	my_str(my_strindex(test1, 'H'));//llol
	my_char('\n');
	
	my_str(my_strnindex(test1, 'l',6));//llol
	my_char('\n');
	my_str(my_strnindex(NULL, 'l',6));//NULL
	my_char('\n');
	my_str(my_strnindex(NULL, '0',6));//NULL
	my_char('\n');
	my_str(my_strnindex(NULL, 'l',-8));//NULL
	my_char('\n');
	my_str(my_strnindex(test1, 'l',-8));//NULL
	my_char('\n');
	my_str(my_strnindex(test1, 'H',7));//Hello1
	my_char('\n');
	my_str(my_strnindex(test1, 'o',3));//NULL
	my_char('\n');
	my_str(my_strnindex(test1, 'o',67));//NULL
	my_char('\n');
	
	my_str(my_strdup(test1));//Hello1
	my_char('\n');
	my_str(my_strdup(NULL));//NULL
	my_char('\n');
	my_str(my_strdup("HI EVERYBODY"));//HI EVERYBODY
	my_char('\n');*/
	
	my_str(my_digits2());
	my_str(my_num_base2(86, my_digits2()));
}
