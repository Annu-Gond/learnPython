n = int(input("Enter an number:"))
for i in range(2,n+1,2):
    print(" "*(n-1),end="")
    print("*"*(i),end="")
    print("")