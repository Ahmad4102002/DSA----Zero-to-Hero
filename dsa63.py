# find the sencond minimum number in an array 

arr = [1, 7, 3, 9, 2]

min1 = float('inf')
min2 = float('inf')

for each in arr:
    if each < min1:
        min2 = min1
        min1 = each
    elif each < min2 and each != min1: # number is greater than first min but smaller than second minimum
        min2 = each


if min2 == float('inf'):
    print("NOT FOUND")
else:
    print(min2)