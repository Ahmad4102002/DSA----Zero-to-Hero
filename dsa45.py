n=5
for i in range(n):
    for j in range(2*(n-i)-1,2*(n),2):
        print(j,end="")
    print()