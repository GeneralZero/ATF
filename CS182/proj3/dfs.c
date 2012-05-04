//dfs.c

#include "mygraph.h"

void dfs(t_graph *g){
	if((g!=NULL)){
		int i;
		for(i=0;i<g->v;i++)
			(g->vertices[i]).visited = FALSE;
		printf("%s\n",g->vertices[0].name);
		for(i=0;i<g->v;i++)
			if((g->vertices[i]).visited == FALSE)
				dfsrecurse(g, i);
	}
}
