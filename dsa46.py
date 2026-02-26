n = 5

for i in range(n):
    for j in range(i+1):
        if j % 2 == 1:
            print(0,end="")
        else:
            print(1,end="")
    print()

