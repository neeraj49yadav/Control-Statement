#WAP to determine triangle types.

A=int(input("Enter first Angle: "));
B=int(input("Enter second Angle: "));
C=int(input("Enter third Angle: "));
if(A+B+C==180):
   if(A and B and C>90):
    print("Obtuse Triangle")
   elif(A and B and C==90):
    print("Right Triangle")
   else:
    print("Acute Triangle")
else:
  print("Not Valid Triangle")