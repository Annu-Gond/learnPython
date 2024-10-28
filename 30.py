def remove(l,word):
    for item in l:
        l.remove(word)
        return l

l = ["Harry","Annu","shruti","tanisha","an"]
print(remove(l,"an"))

