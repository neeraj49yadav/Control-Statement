'''Q9. Take an integer N as input. Your task is to calculate and print the sum of the digits of the
given number N.'''

num=int(input("enter number="));
sum=0
while num != 0:
    r=num%10
    num=num//10
    sum=sum+r
print(sum)