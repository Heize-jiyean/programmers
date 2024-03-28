import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
	    
	    Scanner in=new Scanner(System.in);
	    int input=in.nextInt();
	    int charge=1000-input;
	    int cnt=0;
	    
	    int[] List={500,100,50,10,5,1};
	    
	    
	   for(int i=0;i<List.length;i++){
	       int coin=List[i];
	       
	       cnt+=charge/coin;
	       charge=charge%coin;
	  
	   }
	    //동전개수출력
	    System.out.println(cnt);
	  
	}
}