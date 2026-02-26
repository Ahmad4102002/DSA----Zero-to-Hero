# Pattern 7: Print circle box number pattern with 1 and 0
rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if i == 0 and j >0 and j < rows-1 or i == cols-1 and j >0 and j < rows-1 or j == 0 and i > 0 and i < rows-1 or j == cols-1 and i > 0 and i < rows-1:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()