"""
Input: nums = [1,2,2,3,3,3], k = 2

Output: [4,3]

"""
nums = [1,2,2,4,4,4,3,3,3] # {1: 1, 2: 2, 4: 3, 3: 3}
k = 2


dicc = {} # {1: 1, 2: 2, 4: 3, 3: 3}

for each in nums:
    dicc[each] = dicc.get(each,0 ) + 1


# remove the key with the max value
new2 = []

for i in range(k):
    max_key = max(dicc,key = dicc.get)
    new2.append(max_key)
    del dicc[max_key]

print(new2)