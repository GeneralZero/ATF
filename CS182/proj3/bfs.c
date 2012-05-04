//bfs.c

#include "mygraph.h"

void bfs(t_graph *g){
	if(g!=NULL){
		int i, k=0;
		for(i=0;i<g->maxv;i++)
			g->vertices[i].visited = FALSE;
		g->vertices[0].visited = TRUE;	
		printf("%s\n", g->vertices[0].name);
		bfswork(g,0);
	}
}		
