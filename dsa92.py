matrix = [
 [9, 3, 5],
 [1, 8, 2],
 [4, 7, 6]
]

# row wise

new_r = []
for i in range(len(matrix)):
    new = []
    for j in range(len(matrix[i])):
        new.append(matrix[i][j])
    
    new.sort()
    new_r.append(new)



# for column wise ---- flip rows and columns
new_c = []
for i in range(len(matrix)):
    mew = []
    for j in range(len(matrix[i])):
        mew.append(matrix[j][i])
    mew.sort()
    new_c.append(mew)

# Convert this new matrix into a row matrix

cew_c = []
for i in range(len(matrix)):
    cew = []

    for j in range(len(matrix[i])):
        cew.append(new_c[j][i])
    cew_c.append(cew)

print(cew_c)