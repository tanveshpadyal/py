
str= input("enter a string to count charaters and digits=")
char =0
count =0
for x in list(str.strip()):
    if x.isalpha():
        char += 1
    elif x.isdigit():
        count += 1

print(f"Numbers of charaters: {char}\nNumbers of digits: {count}")