# Check if Three Elements Exist with a Sum Equal to a Target Value

arr = [1, 4, 45, 6, 10, 8]
target = 22

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if arr[i]+arr[j]+arr[k] == target:
                print(f"FOUND: {arr[i]} + {arr[j]} + {arr[k]}",)