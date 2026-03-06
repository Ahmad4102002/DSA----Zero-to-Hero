"""
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

"""


nums = [1,2,2,3,3,3]

k = 2  # to most frequent numbers


dicc = {}

for each in nums:
    dicc[each] = dicc.get(each,0) +1 



all_keys = dicc.keys()

for each in all_keys:
    print(each)


