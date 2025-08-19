//Q5. Read a number check if it is divisible by 7 or its last digit is 5.

import java.util.Scanner;
class no 
{
 public static void main (String args[])
 {
  int n;
  Scanner sc=new Scanner(System.in);
  System.out.print("\n Enter n:");
  n=sc.nextInt();
  if(n%7==0 || n%10==5)
   System.out.print("\n divisible by 7 or its last digit is 5 ");
  else
   System.out.print("\n It is not divisible by 7 or last digit is not 5 ");
 }
}