# WAP to input three no and print the maximum among them.
A=int(input("Enter first value: "));
B=int(input("Enter second value: "));
C=int(input("Enter third value: "));

if(A>B and A>C):
    print("A is the maximum value")
elif(B>A and B>C):
    print("B is the maximum value")
else:
    print("C is the maximum value")
