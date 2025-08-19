//Q1. Eligible to vote excercise question using if-else statements.

import java.util.Scanner;
class Eligible
{
 public static void main (String args[])
 {
  int age;
  Scanner sc=new Scanner(System.in);
  System.out.print("\n Enter age:");
  age=sc.nextInt();
  
  if(age>=18)
    System.out.print("\n Eligible to vote ");
  else
    System.out.print("\n Not eligible to vote ");
 }
}
  