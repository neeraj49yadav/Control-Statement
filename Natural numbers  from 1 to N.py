'''Q1. Write a program that takes a positive integer N as input from the user and prints all natural numbers
numbers from 1 to N, with each number followed by a space.'''

num=int(input("enter number="))
a=1
for i in range(num):
    print(a,end=" ")
    a=a+1