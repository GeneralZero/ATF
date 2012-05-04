//my_num_base.c

#include "../lib/my.h"

void my_num_base(int num, char* string)
{
	unsigned int exp;
	unsigned int u;
	unsigned int base;

	if(string !=NULL && (base = my_strlen(string)) > 0)
	{
		u=num;
		if (num <0){
			my_char('-');
			u = num * -1;
		}
	
		if(base==1)
			while(u-->0)
				my_char(*string);
				
		else
		{
			for(exp=1;(u/exp)>=base ;exp*=base);
			
			for(; exp; u%=exp, exp/=base)
				my_char(string[u/exp]);
		}
		my_char('\n');
	}
	else
		my_str("Invalid Base.");
}
	
