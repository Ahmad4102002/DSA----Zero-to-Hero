for i in range(6):
    for k in range(6-i):
        print(" ", end=" ")

    for j in range(i):
        if j == 0 or j == i-1 or i == 5:
            print("*", end =" ")
        else:
            print(" ",end =" ")
    print()