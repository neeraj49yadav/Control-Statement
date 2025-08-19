//Q2. read a number and check if it is divisible by 7.
import java.util.Scanner;
class divisible
{

 public static void main (String args[])
 {
  int n;
  Scanner sc=new Scanner(System.in);
  System.out.print("\n Enter n:");
  n=sc.nextInt();
  
  if(n%7==0)
    System.out.print("\n Divisible by 7 ");
  else
    System.out.print("\n Not divisible by 7 ");
 }
}
  