def greatest():
    a = int(input("Enter 1st num:"))
    b = int(input("Enter 2nd num:"))
    c = int(input("Enter 3rd num:"))

    if(a>b and a>c):
        print(f"Greatest number is {a}")
    elif(b>a and b>c):    
        print(f"Greatest number is {b}")
    else:
        print(f"Greatest number is {c}")

greatest()