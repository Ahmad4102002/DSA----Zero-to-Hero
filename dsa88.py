# Problem Statement: Print Upper and Lower Triangle of a Matrix


matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]



# CREATE  A NEW  MATRIX COPY TRIAGLE but replace zeros 


new_mat = []

for i in range(len(matrix)):
    mat = []
    for j in range(len(matrix[i])):   # [1, 2, 3]  if j == i   0,1,2
        if j < i:
            mat.append(0)
        else:
            mat.append(matrix[i][j])
    new_mat.append(mat)

print(new_mat)

