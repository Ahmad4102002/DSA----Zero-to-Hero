# Pattern 3: Print box number pattern of 1s and 0s
rows = 6
cols = 5

for i in range(rows):
    for j in range(cols):
        if i ==0 or i == rows-1 or j == 0 or j == cols -1:
            print(1,end =" ")
        else:
            print(0,end=" ")
    print()