word = "Donkey"

with open("donkey.txt","r") as f:
    Content = f.read()

new = Content.replace(word,"######")

with open("donkey.txt","w") as f:
    f.write(new)
