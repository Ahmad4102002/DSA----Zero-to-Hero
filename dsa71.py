s = "programming"

dicc = {}

for each in s:
    dicc[each] = dicc.get(each,0) + 1 



max_num = float('-inf')
min_num = float('inf')

for values in dicc.values():
    if values > max_num:
        max_num = values 
    if values < min_num:
        min_num = values

print(max_num)
print(min_num)