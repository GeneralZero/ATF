//main.c

#include "mygraph.h"

int main(int argc, char **argv){
	t_heap* theHeap = newHeap(10);
	t_graph* theuGraph; //= new_digraph(10);
	t_graph* thedGraph;
	t_graph* prims;
	int i,j,k;
	int** arrg;
	int* array;
	
	theuGraph = parceu("test.txt");
	thedGraph = parce("test.txt");
	//show_am(thedGraph);
	//show_am(theuGraph);
	while(i!=0){
		i=menu();
		if(i==1){
			char new[100];
			scanf("%s",new);
			theuGraph = parceu(new);
			thedGraph = parce(new);
		}
	
		if(i==2){
			bfs(thedGraph);
		}	
	
		if(i==3){
			dfs(thedGraph);
		}
	
		if(i==4){
			if(thedGraph!=NULL){
				printf("Insert a vertex from 0 to %d:",thedGraph->maxv-1);
				scanf("%d",&j);
				prims = prim(thedGraph, j);
				show_am(prims);
			}
		}

		if(i==5){
			if(thedGraph!=NULL){
				printf("Insert a vertex from 0 to %d:",thedGraph->maxv-1);
				scanf("%d",&j);
				array = dijkstra(thedGraph, j);
			
				for(j=0; j<thedGraph->maxv; j++)
					printf("%d ",array[j]);
				printf("\n");
			}
		}

		if(i==6){
			if(theuGraph!=NULL){
				arrg = floyd(theuGraph);
				for(k=0; k<theuGraph->maxv; k++){
					printf("\n");
					for(j=0; j<theuGraph->maxv; j++)
						printf("%d ",arrg[k][j]);
				}
				printf("\n");
			}
		}

		if(i==7){
			printf("This is currently under Construction");
			//fordFulkerson(theuGraph, 0, 3);
		}
	}
}
