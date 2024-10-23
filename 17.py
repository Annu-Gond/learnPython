m1 = int(input("Enter marks:"))
m2 = int(input("Enter marks:"))
m3 = int(input("Enter marks:"))

total_per = (m1+m2+m3)/300*100
# print(total_per)
if(total_per >= 40 and m1>33 and m2>33 and m3>33):
    print("You passed!")

else:
    print("Sorry, you failed :(")    

print("Your percentage is:",int(total_per),"%")    