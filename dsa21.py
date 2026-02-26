# Pattern 6: Print box number pattern of 1 and 0 with cross center

rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if j == i or j == rows-i-1:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()