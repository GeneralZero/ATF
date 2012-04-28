#include <iostream>
#include <fstream>
#include <string>
int main()
{       int t,i,j,len,CASE,base;
        char az[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
        char str[102],tmp;
        CASE=1;
        ifstream myfile ("A-small-attempt0.in");
        if (myfile.is_open())
        {
			while ( myfile.good() )
			{
				  getline(myfile,tmp);
				  len=strlen(tmp);
				  printf("Case #%d: ",CASE++);
				  cout << line << endl;
				  for(i=0;i<len;i++)
                	{       base=str[i]-'a';
                        if(base>=0&&base<=25)
                                printf("%c",az[base]);
                        else
                                printf(" ");
                }
                printf("\n");
			}
			myfile.close();
		}
        printf("END");
        return 0;
}
