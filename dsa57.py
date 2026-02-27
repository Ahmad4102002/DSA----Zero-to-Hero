arr = [1, 2, 3, 4, 5,3]
    #  0, 1, 2, 3, 4

#AGAIN

# check if an array is sorted in ascenndig order or not 

is_ascending = True
is_descending = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_ascending = False
    if arr[i] < arr[i+1]:
        is_descending = False



if is_ascending:
    print("Ascending")
elif is_descending:
    print("Descending")
else:
    print("Not Sorted")

