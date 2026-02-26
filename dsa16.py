# Pattern 1: Print 1, 0 number pattern at alternate rows

rows = 6
cols = 5

for i in range(rows):
    for j in range(cols):
        if i % 2 == 0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()