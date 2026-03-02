# Calculate the Sum of Each Row and Each Column in a Matrix

matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

# ROW 

for i in range(len(matrix)):
    sum = 0
    for j in range(len(matrix[i])):
        sum += matrix[i][j]
    print(sum, end = " ")



# COLUMN 

for i in range(len(matrix)):
    sum = 0 
    for j in range(len(matrix[i])):
        sum += matrix[j][i]
    print(sum, end = " ")
