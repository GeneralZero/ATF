package cgreco;

public class Chambers{
	public int size;
	public int guests;
	public int[] Chambers;
	public Chambers(){
		size = 10;	
		guests = 0;
		Chambers = new int[10];
	}
	public Chambers(int s){
		size = s;	
		guests =0;
		Chambers = new int[s];
	}
}
