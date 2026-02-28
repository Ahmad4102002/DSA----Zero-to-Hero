# Find the second maximum number in an array 


arr = [1, 7, 3, 9, 2]

max1 = float('-inf')
max2 = float('-inf')


for each in arr:
    if each > max1:
        max2 = max1
        max1 = each

    elif each > max2 and each != max1:
        max2 = each 
    

if max2 == float('-inf'):
    print("NOT FOUND")
else:
    print(max2)