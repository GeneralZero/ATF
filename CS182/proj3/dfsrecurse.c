//dfsrecurse.c

#include "mygraph.h"

void dfsrecurse(t_graph *g, int k){
	if((k>=0)&&(g!=NULL)&&(k<=g->maxv)){
		int i;
		//printf("%d: %s\n",k,g->vertices[k].name);
		for(i=0;i<g->maxv;i++)
			if((g->am[k][i]!=0)&&((g->vertices[i]).visited == FALSE)){
				printf("%s\n",g->vertices[i].name);
				g->vertices[i].visited = TRUE;
				dfsrecurse(g,i);
			}
	}
}
