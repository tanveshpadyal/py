
ele = [1,2,3,4,5]
li = []
for x in range(len(ele)):
    tup = (ele[x], ele[x] * ele[x])
    li.append(tup)

print(li)

