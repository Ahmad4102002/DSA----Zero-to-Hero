# Check if matrix is symetric 

matrix = [
 [1, 2, 3],
 [2, 5, 6],
 [3, 6, 9]
]

is_symetric = True
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != matrix[j][i]:
            is_symetric=False

print(is_symetric)
