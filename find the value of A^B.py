#Q12. You are given two integers A and B. You have to find the value of A^B.

A=int(input("enter the first value="))
B=int(input("enter the second value="))
ans=1
for i in range(B):
    ans=ans*A
print(ans)