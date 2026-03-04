#Check if a Matrix is an Identity Matrix

matrix = [
 [1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]
]
# only element at 

is_Identity = True 

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j == i:
            if matrix[i][j] != 1:
                is_Identity = False
                break
        if i!= j:
            if matrix[i][j] != 0:
                is_Identity = False
                break
    if not is_Identity:
        break
print(is_Identity)