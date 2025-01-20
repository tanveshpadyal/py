

strname ="myname is tillu"
newstr =""
newcount =""
for x in range(len(strname)):
    if x % 2 == 0:
        newstr += strname[x]
    else:
        newcount += str(x);

print(newstr)
print(newcount)