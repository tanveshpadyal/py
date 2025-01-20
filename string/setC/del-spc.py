

str1 = "/*Sachin is @Cricketer& kind person"

newstr = ""

for x in str1:
    if x.isalpha():
        newstr += x
    elif x.isspace():
        newstr += x

print(newstr)