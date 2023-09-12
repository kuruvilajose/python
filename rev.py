a=int(input("Enter a number ")) 
rev=0
dig=0
while (a!=0):
    dig=a%10
    rev=rev*10+dig
    a=a//10
print("rev num=",rev)   