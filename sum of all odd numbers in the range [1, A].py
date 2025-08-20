'''Q7. Take an integer A as input. You have to print the sum of all odd numbers in the range [1,
A].'''

num = int(input("Enter num: "))
sum = 0

for i in range(1, num + 1):
    if i % 2 == 1:   
        sum += i

print("The sum of given range of even number :", sum)