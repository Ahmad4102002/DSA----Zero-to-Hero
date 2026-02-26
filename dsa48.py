n = 5
k = 1 
for i in range(n):
    for j in range(i+1):
        if k % 2 == 1:
            print(1,end="")
        else:
            print(0,end="")
        k+=1
    print()


    # odd ,  