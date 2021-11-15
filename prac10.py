#program to calculate the average of two numbers
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
avg=(num1+num2)/2
dev1=num1-avg
dev2=num2-avg
print("Average="+str(avg))
print("Deviation of first number="+str(dev1))
print("Deviation of second number="+str(dev2))