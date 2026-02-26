# right arrow star pattern
# 0 1 2 3 4 
n=5
for i in range(n-1):
    for k in range(2*i):
        print(" ",end =" ")
    for j in range(n-i):
        print("*",end=" ")
    print()

for i in range(n):
    for k in range(2*(n-1)-(2*i)):
        print(" ",end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
