//Q4. Check if its divisible by 3 and its last digit is 4.

import java.util.Scanner;
class Divisible
{
 public static void main (String args[])
 {
  int n;
  Scanner sc=new Scanner(System.in);
  System.out.print("\n Enter n:");
  n=sc.nextInt();
  if(n%3==0 && n%10==4)
   System.out.print("\n divisible by 3 and its last digit is 4 ");
  else
   System.out.print("\n It is divisible by 3 and last digit is not 4 ");
 }
}