str = "hello"
list1 = []
list2 = []



# Iterate through the unique characters in the string
for char in set(str):
    count = 0
    for c in str:  # Count occurrences of the character
        if c == char:
            count += 1
    print(char, count)
