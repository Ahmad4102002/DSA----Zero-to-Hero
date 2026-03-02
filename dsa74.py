s =  "The quick brown fox jumps over the lazy dog"



# put every elemt in a set

letters = set()

for each in s:
    letters.add(each)

d = "abcdefghijklmnopqrstuvwxyz"


for each in d:
    if each not in letters:
        print(f"String doe snot contain letter {each}")
        break 
else:
    print("ALL GOOD ")