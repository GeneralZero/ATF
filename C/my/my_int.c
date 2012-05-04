//my_int.c

#include "../lib/my.h"

void my_int(int num)
{
	unsigned int exp;
	unsigned int u;
	unsigned int base = 10;
	
	u=num;
	if (num <0){
		my_char('-');
		u = num * -1;
	}
		
	for(exp=1;(u/exp)>=base ;exp*=base);
	
	for(; exp; u%=exp, exp/=base)
		my_char('0'+(u/exp));
		
	my_char('\n');
}
	
