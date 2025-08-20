'''Q2. Write a program to print all Natural numbers from N to 1, where you have to take N as input
from the user.'''

num=int(input("enter number="))
a=num
for i in range(num):
    print(a,end=" ")
    a=a-1