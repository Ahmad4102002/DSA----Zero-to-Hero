rows = 5
cols = 5

for i in range(rows):
    if i % 2 == 0:
        n = 0
    else: 
        n = 1
    for j in range(cols):
        if j % 2 == n:
            print(1,end=" ")
        else:
            print(0,end= " ")
    print()