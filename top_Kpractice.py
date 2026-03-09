"""

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2


Output: [2,3]

"""

nums = [1,1,2,2,3,3,3]
k = 2

liss = [ [] for i in range (len(nums) + 1) ]

# make a hash map frequency 

#  make a data structure looking like this
# [[],[],[],[]]


freq = {}

for each in nums:
    freq[each] = freq.get(each,0) + 1
print(freq)

for key,value in freq.items():
    liss[value].append(key)

print(liss)

final = []

for i in range(len(liss)-1,-1,-1):
    for each in liss[i]:
        if k > 0:
            final.append(each)
            k-=1

print(final)
