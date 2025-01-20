
str1 = "hello"
str2 = "world"

ms = str1[:2]
ms2 =  str2[:2]

a = str1.replace(ms, ms2)
b = str2.replace(ms2, ms)

print(a+b)