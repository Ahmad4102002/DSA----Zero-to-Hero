# hollow star with a diagonal
n = 10
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == 0 or i == n-1:
            print("*", end= " ")
        elif i == j:
            print("*", end= " ")
        elif j == n-i-1:
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print()


# how will we know it is a fiagonal point