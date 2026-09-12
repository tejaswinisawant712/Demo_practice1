a=int(input("Enter first no:"))
b=int(input("Enter second no:"))
c=int(input("Enter third no:"))

if a>=b and a>=c:
    print("Largest no:",a)

elif b>=a and b>=c:
    print("Largest no:",b)

else:
    print("Largest no:",c)    
