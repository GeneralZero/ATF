package cgreco;

public class Person {
	String name;
	String Surname;
	int TBLevel;
	int Cake;
	int Age;
	boolean played;
	public Person(){
		name="";
		Surname= "";
		TBLevel=0;
		Cake=0;
    		Age=0;
		played = false;
	}

	public Person(String n){
		name = n;
		Surname = "";
		TBLevel =0;
		Cake =0;
    		Age =0;
		played = false;
   	}
	@Override
	public String toString(){
		return name + " " +Surname + " TBlevel: " + TBLevel +" Cake: " + Cake + " Age: " + Age;
	}
}
