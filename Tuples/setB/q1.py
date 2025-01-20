
tup = (11,666,6546,15)
tup2 = ('h','l','l','o')
newstring=""

for x in tup:
    newstring += str(x)
    newstring += " "

print(newstring)


demo = "".join(map(str,tup))

print(demo)

