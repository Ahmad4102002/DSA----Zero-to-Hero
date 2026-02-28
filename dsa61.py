# Find the maximum number

arr = [-5, -2, -9, -1]

temp = arr[0]
temp1 = arr[0]
for each in arr:
    if each > temp:
        temp = each
    if each < temp1:
        temp1 = each

print(temp)
print(temp1)

