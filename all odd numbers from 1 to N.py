'''Q4. Write a program to print all odd numbers from 1 to N, where you have to take N as input
from user.'''

num=int(input("enter number="))
a=1
for i in range(num):
    if (a%2==1):
        print(a,end=" ")
    a=a+1