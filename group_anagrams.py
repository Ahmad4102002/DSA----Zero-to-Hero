"""
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

"""

strs = ["act","pots","tops","cat","stop","hat"]

anagrams = {}



for each in strs:
    count = [0] * 26  # creating identity of letters in  a 26 0 array 
    for letter in each:
        count[ord(letter) - ord('a') ] += 1
    
    key = tuple(count)

    if key not in anagrams:
        anagrams[key] = []
    anagrams[key].append(each) # {(1,0,1,0,0,0,0,1,0,,) : act}

    result = list(anagrams.values())
print(result)