# Delete an Element at the Xth Position, Shifting Left

arr = [4,7,3,9,5]
x = 3 

idx = x-1

for i in range(idx, len(arr) - 1):
    arr[i] = arr[i + 1]