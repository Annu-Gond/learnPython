d = {}
for i in range(0,5):
    name = input("Enter your name:")
    lang = input("Enter you language:")
    d.update({name : lang})

print(d)
