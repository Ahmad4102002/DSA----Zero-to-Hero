rows = 5
cols = 5


for i in range(rows):
    for k in range(cols-i-1):
        print(rows-i, end="")
    for j in range(cols-i,cols + 1):
        print(j, end="")
    print()