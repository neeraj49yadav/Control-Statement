#WAP to state that triangle is valid or not.

A=int(input("Enter first Angle: "));
B=int(input("Enter second Angle: "));
C=int(input("Enter third Angle: "));

if (A+B+C==180):
    print("Triangle is valid")
else:
    print("Triangle is not valid")