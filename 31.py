f = open("poem.txt" )
c = f.read()
if("Twinkle" in c):
    print("It is present")
else:
    print("It is not present")    

f.close()