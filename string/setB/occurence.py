sen = "Enetr your name name";
 
mode_sen = sen.split(" ");
# list = []

for x in set(mode_sen):
    c = mode_sen.count(x)
    # count = 0
    # for word in mode_sen:
    #     if x == word:
    #         count += 1
    print(x,c)