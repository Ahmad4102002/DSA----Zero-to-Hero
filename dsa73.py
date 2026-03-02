# Find the First and Last Index of Occurrence for Each Character in a String

s = "programpmipng"

n = len(s)

for j, ch in enumerate(s):

    first_index = j
    last_index = j

    for i in range(n):
        if s[i] == ch:
            last_index = i

    print(f"{ch} -> First: {first_index}, Last: {last_index}")
            

