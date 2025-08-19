# WAP to print grade of Student

A=float(input("Enter the percentage="));

if(A>85 and A<=100):
    print("Grade A+") 

elif(A>65 and A<=85):
    print("Grade A")
    
elif(A>45 and A<=65):
    print("Grade B")
    
elif(A>25 and A<=45):
    print("Grade C")
    
else:
    print("Grade D")