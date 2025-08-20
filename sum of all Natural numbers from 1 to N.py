'''Q5. Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as
input from user.'''

num=int(input("enter number="))
sum=0
for i in range(1, num + 1):
    sum =sum+ i  

print("The sum of given range of natural number :", sum)