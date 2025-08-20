'''Q3. Write a program to print all even numbers from 1 to N, where you have to take N as input
from the user.'''

num=int(input("enter number="))
a=1
for i in range(num):
    if (a%2==0):
        print(a,end=" ")
    a=a+1