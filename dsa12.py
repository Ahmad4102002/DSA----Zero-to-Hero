# inverted pyraamid
n=5
for i in range(n):
    for k in range(i):
        print(" ",end=" ")
    for j in range(2*n-1 - 2*i):
        print("*",end= ' ')
    print() 