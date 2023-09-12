import math
a=int(input("Enter a number ")) 
sum=0
temp=a
while (a!=0):
    sum=sum+math.factorial(a%10)
    a=a//10
print("sum is",sum)        
if sum==temp:
    print("it is a strong number")   
else:
    print("it is not a strong number")    