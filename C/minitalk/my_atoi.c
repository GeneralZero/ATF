//my_atoi.c

#include "../lib/my.h"

int	my_atoi(char* s_int)
{
	char flag=1;
	if(s_int[0] == '-')
	{
		flag = -1;
		s_int = &s_int[1];
	}
	int i;
	int ret;
	for(i=0, ret =0 ; s_int[i]!='\0' && s_int[i]!='.'; i++)
	{
		ret *= 10;
		ret += s_int[i] -  '0';
		//my_int(s_int[i] -  '0');
		//my_int(ret);
	}
	return	ret*flag;
}
/*
int	main(int argc,char** argv)
{
	my_int(my_atoi(argv[1]));
}
*/
