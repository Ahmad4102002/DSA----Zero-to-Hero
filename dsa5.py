# mirrored right triangle tar pattern

for i in range(6):
    for k in range(6-i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end =" ")
    print()