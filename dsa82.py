arr = [2, 1, 5, 1, 3, 2]
k = 3

sum = 0 
left = 0

max_sum = float('-inf')

    # sliding window length shoul dnot exceed k 
for right in range(len(arr)):
    sum += arr[right]
    while(right - left + 1 > k):  # when it exceeds
        sum -= arr[left]
        left += 1

    if (right - left +1 ) == k:
        max_sum = max(max_sum,sum)

print(max_sum)
