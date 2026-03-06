"""Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
"""

strs = ["act","pots","tops","cat","stop","hat"]

# i want to make a dictionary with  dicc = {key, value }  key is  tuple identity ([1,0,0,0,1,1,0,0,0]) and values are list of items with same identity  

anagrams = {}

for each in strs:
    count = [0] * 26

    for every in each:                # V +1 flips 0 to 1 
        count[ord(every) - ord('a')] += 1 
        #  ^^ this determines the index 
    key = tuple(count)


    if key not in anagrams:
        anagrams[key] = []
    anagrams[key].append(each)

results = list(anagrams.values())
print(results)
