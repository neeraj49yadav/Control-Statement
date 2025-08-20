'''Q6. You are given an integer A, you need to find and return the sum of all the even numbers
between 1 and N.'''


num = int(input("Enter num: "))
sum = 0

for i in range(1, num + 1):
    if i % 2 == 0:   
        sum += i

print("The sum of given range of even number :", sum)

