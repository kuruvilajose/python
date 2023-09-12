x=int(input("first number"))
y=int(input("second number"))
print("1.add")
print("2.sub")
print("3.multiplication")
print("4.div")
a=int(input("operation"))

if a==1:
 sum=x+y
 print("sum is",sum)
elif a==2:
 sum=x-y
 print("difrence is",sum) 
elif a==3:
 sum=x*y
 print("product",sum)
elif a==4:
 sum=x/y
 print("quationt is",sum) 
else:
 print("invalid")
