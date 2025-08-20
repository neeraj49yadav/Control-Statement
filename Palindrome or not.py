'''Q10. You are given an integer A as input, and you need to determine whether it is a palindrome
or not.'''

num = int(input("Enter number: "))
temp = num    
rev = 0

while num != 0:
    r = num % 10
    rev = (rev * 10) + r
    num = num // 10 

if temp == rev:
    print("Palindrome")
else:
    print("Not palindrome")
