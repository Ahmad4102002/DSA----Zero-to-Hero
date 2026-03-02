#  Problem: Longest Subarray with Sum ≤ K

arr = [1, 2, 1, 0, 1, 1, 0]
k = 4

left = 0 

curr_sum = 0 

max_length = 0 

for right in range(len(arr)):
    curr_sum += arr[right]

    while(curr_sum > k):
        curr_sum -= arr[left]
        left += 1 
    
    length = right - left + 1
    max_length = max(max_length,length)
    

print(max_length)


"""
DRY RUN 

0 index 
curr sum = 1

while will not run since 1 is not greater than 4

length calculated 

"""