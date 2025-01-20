

tup = (1,2,3,5,3,4,2,6,8,6)

for x in set(tup):
    count = tup.count(x)
    if(count >=2 ):
        print(x)
