sidea=float(input("enter lenght of side a: "))
sideb=float(input("enter lenght of side b: ")) 
sidec=float(input("enter lenght of side c: "))
squarea=sidea**2
squareb=sideb**2 
squarec=sidec**2
if(squarea+squareb==squarec): 
    print("it is right-angled trangle")
elif(squarea+squarec==squareb): 
    print("it is right-angled trangle")    
elif(squarec+squareb==squarea): 
    print("it is right-angled trangle")        
else:
    print("it is not right-angled triangle")
