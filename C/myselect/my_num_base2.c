//my_num_base2.c

#include "../lib/my.h"

char* my_num_base2(int num, char* string)
{
	unsigned int exp;
	unsigned int u;
	unsigned int base;
	int i=0;
	
	
	for(u=0, base=10, exp=1; num/exp> 1; exp*=base, u++);

	//my_str(string);
	
	char* ret = (char*)my_xmalloc((u+2)*sizeof(char));

	if(string !=NULL && (base = my_strlen(string)) > 0)
	{
		//my_str("w");
		u=num;
		if (num <0){
			ret[i++] = '-';
			u = num * -1;
		}
		//my_str("e");
		if(base==1)
			while(u-->0)
				ret[i++] = *string;
		
		else
		{
			//my_str("r");
			
			for(exp=1;(u/exp)>=base ;exp*=base);
			//my_str("t");
			for(; exp; u%=exp, exp/=base)
			{
				//my_int(exp);
				//my_int(u);
				ret[i++] = string[u/exp];
				//my_char(string[u/exp]);
			}
			//my_str("y");
		}
		ret[i++] = '\0';
		//my_char('\n');
	}
	else
		my_str("Invalid Base.");
		
	return ret;
}
	
