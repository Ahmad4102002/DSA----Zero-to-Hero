# in place inertion array 
arr = [4, 7, 3, 9, 5]
x = 3 # index to be replaced -1
value = 10

idx = x - 1

arr.append(0)
for i in range(len(arr)-1,idx,-1):
    arr[i] = arr[i-1]

arr[idx]= value

print(arr)
