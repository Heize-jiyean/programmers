import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
	    
	    Scanner in=new Scanner(System.in);
	   
	    int N=in.nextInt();
	    int K=in.nextInt();
	    
	    int[] Array= new int[N];
	    for(int i=0;i<N;i++){
	        Array[i]=in.nextInt();
	    }
        
	    int cnt=0;
        
        //개수 계산(배열을 거꾸로 순회)
	    
	    for(int i=N-1;i>=0;i--){
	        
	        if(K>=Array[i]){
	            cnt+=K/Array[i];
	            K=K%Array[i];
	        }
	    } 

        System.out.println(cnt);

	}
}