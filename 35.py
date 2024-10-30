words = ["Donkey","chhii","kutta","bekar"]

with open("donkey.txt","r") as f:
    Content = f.read()
for i in words:
    Content = Content.replace(i,"#"*len(i))

with open("donkey.txt","w") as f:
    f.write(Content)
