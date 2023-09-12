lim2=int(input("Enter lowerlimit ")) 
lim1=int(input("Enter upperlimit ")) 
a=lim2
while a<=lim1:
    if a%2!=0:
        print(a,"odd")
    a+=1
a=lim2    
while a<=lim1:
    if a%2==0:
        print(a,"enven")
    a+=1    