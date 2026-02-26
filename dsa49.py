n = 5

for i in range(n):
    for j in range(i+1):
        if j == 0 or i == n-1 or j == i:
            print(1,end="")
        else:
            print(0,end="")
    print()