# DIAgonal

matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

new_mat = []
for i in range(len(matrix)):
    new = []
    for j in range(len(matrix[i])): # [1, 2, 3] here i = 0   i want to print zeros according to i     
        if j == i:
            new.append(0)
        else:
            new.append(matrix[i][j])
    new_mat.append(new)

print(new_mat)