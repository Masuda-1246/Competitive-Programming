import java.util.Scanner;
 
public class risa1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
      	 int i = sc.nextInt();
        String hex = Integer.toHexString(i);
        if(hex.length() == 1) System.out.println("0"+hex.toUpperCase());
      	else System.out.println(hex.toUpperCase());
    }   
}