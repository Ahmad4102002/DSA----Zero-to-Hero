"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

"""


strs = ["act","pots","tops","cat","stop","hat"]

anagrams = {}

# create identities of eahc word 




for each in strs:
    counter = [0] * 26 
    for every in each:
        counter[ord(every)- ord('a')] +=1  # [0][0][1][1][1][0][0][0][0]

    key = tuple(counter)

    if key not in anagrams:
        anagrams[key] = []

    anagrams[key].append(each)

results = list(anagrams.values())

print(results)


        