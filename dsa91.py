# Print the Boundary Elements of a Matrix

matrix = [
 [1,  2,  3,  4],
 [5,  6,  7,  8],
 [9, 10, 11, 12]
]

# always print i = 0 and i = len(matrix)




for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == 0 or i == len(matrix) - 1 or j == 0 or j ==len(matrix[i]) -1:
            print(matrix[i][j], end = " ")
    print()