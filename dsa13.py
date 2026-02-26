# hollow inverted pyramid

n=5
for i in range(n):
    for k in range(i):
        print(" ",end=" ")
    for j in range(2*n-1 - 2*i):
        if j == 0 or j == (2*n-1 - 2*i - 1) or i ==0:
            print("*",end= ' ')
        else:
            print(" ",end =" ")
    print()