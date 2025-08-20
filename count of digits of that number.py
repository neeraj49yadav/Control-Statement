#Q8. Take an integer N as input and print the count of digits of that number.

num=int(input("enter number="));
count=0
while num != 0:
    count += 1
    num=num//10
print(count)