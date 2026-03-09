"""
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

"""


nums = [1,2,2,2,3,3,3]

k = 2  # to most frequent numbers


count = {}                                  
freq = [[] for i in range(len(nums) + 1)] # [[],[],[],[],[],[],[]]
                                          #  0 , 1, 2, 3, 4, 5, 6
print(freq)
for n in nums:
    count[n] = 1 + count.get(n, 0) # {1 : 1, 2:2, 3:3 }

for key,value in count.items():
    freq[value].append(key)
    # freq[index].append(num which has tha count)
print(freq)

final = []
for i in range(len(freq)-1,-1,-1):
    for j in range(len(freq[i])):
        if k > 0:
            final.append(freq[i][j])
            k -=1 

print(final)
# [[], [1], [2], [3], [], [], []]  freq will look like this








# BASICALLY THIS is BUCKLET SORT 

# create an array of size of teh original array to be sorted

#  0  1  2  3  4  5  6  -----> count (indexes)
# [] [] [] [] [] [] []  -----> each will have each values which have frequescy == their index 


# lastly traverse this array from the back 
        # if list not empty 
            # append into new list , k -=1
                # check for another teill k = 0