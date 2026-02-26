# triangular number patters 1 inverse

n=5

for i in range(n):
    for k in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        print(i+1,end="")
    print()
