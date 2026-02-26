rows = 5
cols = 5

for i in range(rows):
    for j in range(i+1):
        print(cols-j,end="")
    for k in range(rows-i-1):
        print(cols-i ,end="")
    print()