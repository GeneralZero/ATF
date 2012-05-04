//floyd.c

#include "mygraph.h"

int **floyd(t_graph* g){
	int i,j,k;
	int** D = (int**)malloc(sizeof(int*)*g->maxv);
	for(i=0;i<g->maxv;i++)
		D[i] = (int*)malloc(sizeof(int)*g->maxv);
	for(k=0;k<g->maxv;k++){
		D[k] = dijkstra(g,k);
		for(i=0;i<g->maxv;i++)
			if(k!=i || D[i][k]!=0)
				for(j=0;j<g->maxv;j++)
					if(k!=j || D[k][j]!=0)
						if(D[i][j]>D[i][k]+D[k][j])
							D[i][j]=min(D[i][j],D[i][k]+D[k][j]);
	}
	return D;
}

int min(int a, int b){
	if(a>b)	
		return b;
	return a;	
}
