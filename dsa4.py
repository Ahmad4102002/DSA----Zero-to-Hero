

# first and last all stars
# otherwise only first and last stars

# print * for first and last

# hollow right triangle
for i in range(6):
    for j in range(i):
        if j == 0 or j == i-1 or i ==5:
            print("*", end= " ")
        else:
            print(" ", end=" ")
    print()