#calculate the area of triangle using heron's formulae
a=float(input("Enter the first side of the triangle:"))
b=float(input("Enter the second side of the traingle:"))
c=float(input("Enter the third side of the triangle:"))
print(a,b,c)
S=(a+b+c)/2
area=(S*(S-a)*(S-b)*(S-c))**0.5
print("Area="+str(area))