unit=float(input("Enter units consumed: ")) 
if unit>=0 and unit<=100:
 cost=4.22
elif unit>=101 and unit<=200:
 cost=5.02
else:
 cost=5.87
total=unit*cost
print(total,"is your electricity bill")