#Q11. Take a number A as input, print its multiplication table having the first 10 multiples.

num=int(input("enter number="))
print("Table of ",num,"is")
for i in range(1, 11):
    table=num*i
    print(table)