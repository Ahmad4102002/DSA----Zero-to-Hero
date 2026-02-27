arr = [1, 2, 2, 3, 4, 4, 4]

dicc = {}

unique = 0 
duplicate = 0
for each in arr:
    dicc[each] = dicc.get(each,0)+1


for each in dicc.keys():
    if dicc[each] == 1:
        unique += dicc.get(each)
    elif dicc[each] > 1:
        duplicate += dicc.get(each)

print(dicc)
print(unique)
print(duplicate)