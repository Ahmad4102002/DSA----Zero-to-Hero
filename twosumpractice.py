nums = [7,7]
k = 1

# most 2 frequent are c and b 

end = [[] for i in range(len(nums)+1)]


hashmap = {}

for i in range(len(nums)):
    hashmap[nums[i]] = hashmap.get(nums[i],0)+1

print(hashmap)

for key , value in hashmap.items():
    end[value].append(key)



liss = []
for i in range(len(end)-1,-1,-1):
    for j in range(len(end[i])):
        if k != 0:
            liss.append(end[i][j])
            k -= 1 
print(liss)

