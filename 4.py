n = int(input("Enter any number:"))

#using while loop
i = 0
while(i<(n+1)):
    print("*"* i)
    i +=1

#using for loop    
for s in range(1,n+1):
    print("*"*s)