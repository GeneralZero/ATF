//show_am.c

#include "mygraph.h"

void	show_am(t_graph* g){
	if(g!=NULL){
		int i,j;
		for(i=0;i<g->maxv;i++){
			printf("\n");
			for(j=0;j<g->maxv;j++)
				printf("%d ", g->am[i][j]);
		}
		printf("\n");
	}
}	
