//Q3. Check if it's last digit is divisible by 4.
import java.util.Scanner;
class Last
{
 public static void main (String args[])
 {
  int n;
  Scanner sc=new Scanner(System.in);
  System.out.print("\n Enter n:");
  n=sc.nextInt();
  if(n%10==4)
   System.out.print("\n Last digit is 4 ");
  else
   System.out.print("\n Last digit is not 4 ");
 }
}
  