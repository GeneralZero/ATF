//show_edges.c

#include "mygraph.h"

void show_edges(t_graph *g){
	if(g!=NULL){
		int i,j;
		for(i=0;(i<g->maxv);i++){
			for(j=0; j<g->maxv;j++){
				if(g->am[i][j]!=0)
					printf("(%d - %d)",i,j);
			}
		}
	}
}
