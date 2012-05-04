//show_vertices.c

#include "mygraph.h"

void show_vertices(t_graph *g){
	if(g!=NULL){
		int i;
		for(i=0; i<g->maxv; i++){
			printf("%s\n",g->vertices[i].name);
		}
	}
}
