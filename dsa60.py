# Check if Three Elements Exist with a Sum Equal to a Target Value

# AGAIN USING SET 

arr = [1, 4, 45, 6, 10, 8]
      #1  4  6   8  10  45
target = 22

n = len(arr)
arr.sort()
for i in range(n-2):
    left = i+1
    right = n-1

    while(left<right):
        total = arr[i] + arr[left] +arr[right]

        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            print(f"FOUND {arr[i]} + {arr[left]} + {arr[right]}")
            break 


