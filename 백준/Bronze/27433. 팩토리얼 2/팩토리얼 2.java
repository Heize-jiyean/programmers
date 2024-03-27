import java.util.Scanner;


public class Main
{
    
    public static long factorial(int n){
	        if(n<=0){ 
                 return 1;
	        }
	      
            else{ return n*factorial(n-1);}
	            
    }

	public static void main(String[] args) {
	    
	    Scanner in=new Scanner(System.in);
	    int n=in.nextInt();
		long answer=factorial(n);
		System.out.println(answer);
	}
}