# Pattern 5: Print box number pattern with plus in center

rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if j == (cols-1)//2 or i ==(rows-1)//2:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()