package cgreco;

import java.io.*;
import java.util.Scanner;
import java.lang.Integer;


public class loadFile{
	public static HTable hash;
	public static Person[] chalengers;
	public static Chambers level;
	public static int size=0;

    public static void main(String args[]){
    int ret = 0;
    int i = 0;
	Person C = new Person();
    Scanner cin = new Scanner(System.in);
	loadfile("cakeparty.dat");
	hash = new HTable(size);
	hashpeople();
    while (ret > 5 || ret < 1){
        System.out.println("1) Load Additon file \n2) Insert New Guest \n3) Display Guest \n4) Start Simulation \n5) Exit");
        ret = cin.nextInt();
        if(ret == 1){
			String name;
			System.out.println("Filename:");
            name = cin.next();
            loadfile("./cgreco/"+name);
        }
        if(ret == 2 ){
            System.out.println("Name: ");
            String name;
            name = cin.next();
			C.name = name;
            
            System.out.println("Surname: ");
            name= cin.next();
            C.Surname = name;
            
            System.out.println("TBLevel: ");
            i= cin.nextInt();
            C.TBLevel = i;
            
            System.out.println("Slices of Cake: ");
            i = cin.nextInt();
            C.Cake = i;
            
            System.out.println("Age: ");
            i = cin.nextInt();
            C.Age = i;
	    
	    chalengers[size++] = C;
	    hash.add(C);
        }
           if(ret==3)
               printGuests();
           if(ret==4){
               
			System.out.println("Slices of cake: ");
            i = cin.nextInt();
			Simulation(i);	
			}
           if(ret==5)
               System.exit(0);
			ret =0;
         }  
    }
    public static void loadfile(String filename){
        File file = new File(filename);
	    FileInputStream fis = null;
    	BufferedInputStream bis = null;
	    DataInputStream dis = null;
		String fline;
		int i=size;
        try{
			fis = new FileInputStream(file);
			bis = new BufferedInputStream(fis);
			dis = new DataInputStream(bis);
            while(dis.available() != 0){
				fline = dis.readLine();
                if(Character.isDigit(fline.charAt(0))){
					//System.out.println("Chamber:" + fline);
					CManipulate(fline);
				}
                else{
					//System.out.println("Person:" + fline);
                    chalengers[i++] = PManipulate(fline);
				}
            }
			size =i;
	}
        catch(Exception e){
            System.out.println("Error: " + e.getMessage());
		}
    }

    public static void CManipulate(String line){
        int end;
        int start = 0;
        int count = 0;
        int i;
        end = line.indexOf('|');
        count = Integer.parseInt(line.substring(start, end));
		//System.out.println(count+" "+start+" "+end);
        level = new Chambers(count);
		start = end+1;
        end = line.substring(start, line.length()).indexOf('|')+start;
		//System.out.println(line.substring(start, end));
        level.guests= Integer.parseInt(line.substring(start, end));
		chalengers = new Person[level.guests*level.size];
        for(i = 0; i< count; i++){
            start = end+1;
            end = line.substring(start, line.length()).indexOf('|')+start;
			if(end<start)
				end = line.length();
			//System.out.println(line.substring(start, end));
            level.Chambers[i]= Integer.parseInt(line.substring(start, end));
        }
    }

    public static Person PManipulate(String line){
        int end;
        int start = 0;
        end = line.indexOf('|');
        Person B = new Person(line.substring(start, end));
        start = end+1;
        end = line.substring(start, line.length()).indexOf('|')+start;
        B.Surname = line.substring(start, end);
        start = end+1;
        end = line.substring(start, line.length()).indexOf('|')+start;
        B.TBLevel = Integer.parseInt(line.substring(start, end));
        start= end+1;
        end = line.substring(start, line.length()).indexOf('|')+start;
        B.Cake = Integer.parseInt(line.substring(start, end));
        start= end+1;
        end = line.length();
        B.Age= Integer.parseInt(line.substring(start, end));
        return B;
    }
	
	public static void printGuests(){
		int i;
		for(i=0; i<size; i++){
			if(chalengers[i]!=null && chalengers[i].played==false)
				System.out.println(chalengers[i].toString() + " in chamber " + chalengers[i].Age%level.size);
			//if(hash.look(chalengers[i].Age)!=null)
				//System.out.println(hash.look(chalengers[i].Age).toString());
		}
	}
	
	public static void hashpeople(){
		int i;
		for(i=0; i<size; i++){
			if(chalengers[i]!=null){
				hash.add(chalengers[i]);
			}
		}
	}
	
	public static void Simulation(int cake){
		int i=-1;	
		Person A = new Person();
		//A = hash.remove(chalengers[i].Age);
		while(i < size-1){
			if(size<=0){
				System.out.println("There are no Contestants");			
				break;	
			}
			i++;
			A = hash.remove(chalengers[i].Age);
			if(A!=null){
				if(A.TBLevel>level.Chambers[A.Age%level.size]){
					if(cake - A.Cake>0){
						System.out.println(A.name + " " + A.Surname + " passed test " + A.Age%level.size+1 + " and ate " + A.Cake + " slices of cake");
						cake = cake - A.Cake;
						A.played=true;
					}
					else if(cake >0){
						System.out.println(A.name + " " + A.Surname + " passed test " + A.Age%level.size + " and ate " + cake + " slices of cake");
						cake = 0;
						A.played=true;
					}
					else{
						System.out.println(A.name + " " + A.Surname + " passed test " + A.Age%level.size + " and ate neurotoxins");
						A.played=true;
					}	
				}
				else{
					System.out.println(A.name + " " + A.Surname + " tried test " + A.Age%level.size + " and failed");
					A.played=true;
				}
			}
	}
}
}


