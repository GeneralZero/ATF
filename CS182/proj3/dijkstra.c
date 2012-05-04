//dijkstra.c

#include "mygraph.h"

int *dijkstra(t_graph *g, int k){
	if(g==NULL || k<0 ||k>g->maxv)
		return NULL;
	int i;
	int* ret = (int*)malloc(sizeof(int)*g->maxv);
	t_edge* temp = (t_edge*)malloc(sizeof(t_edge));
	t_heap* theHeap = newHeap(g->maxv);
	for(i=0;i<g->maxv;i++)
		g->vertices[i].visited = FALSE;
	g->vertices[k].visited = TRUE;
	for(i=0;i<g->maxv;i++){
		ret[i] = g->am[k][i];
		if(g->am[k][i]!=0){
			addMaxElement(theHeap,(void*)new_edge(k,i,g->am[k][i]),&eecomp);
		}
	}
	while(theHeap->current_size>0){
		temp = (t_edge*)popMaxHeap(theHeap,&eecomp);
		g->vertices[temp->dst].visited = TRUE;
		for(i=0;i<(g->maxv);i++){
			if(g->am[temp->dst][i]!=0&&g->vertices[i].visited ==FALSE){
				addMaxElement(theHeap,(void*)new_edge(temp->dst,i,g->am[temp->dst][i]),&eecomp);
				if(ret[i]<min(ret[temp->dst],g->am[temp->dst][i])||(ret[i]==0&&ret[temp->dst]!=0)){
					ret[i]=min(ret[temp->dst],g->am[temp->dst][i]);
				}
			}
		}
	}
	return ret;	
}

