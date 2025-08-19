# WAP to input three no and print the minimum among them.
A=int(input("Enter first value: "));
B=int(input("Enter second value: "));
C=int(input("Enter third value: "));

if(A<B and A<C):
    print("A is the mimimum value")
elif(B<A and B<C):
    print("B is the mimimum value")
else:
    print("C is the mimimum value")
