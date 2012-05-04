//menu.c

#include "mygraph.h"
	
int menu(){
	char number = '8';
	while(number < '0' || number > '7'){
		printf("\n1) Import Map \n");
		printf("2) View Map \n");
		printf("3) See Possible Long Paths \n");
		printf("4) Art Exhibit Setup \n");
		printf("5) Direct Traffic from point \n");
		printf("6) Control Masses \n");
		printf("7) Set up the parade! \n");
		printf("0) Exit the program \n\n");
		//fflush(stdin);
		number = getchar();
		//getc(number);
		
	}
	return number-'0';

}
