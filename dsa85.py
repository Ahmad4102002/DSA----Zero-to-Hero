# Find the Maximum and Minimum Values in Each Row of a Matrix

matrix = [
 [3, 5, 1],
 [7, 2, 8],
 [4, 9, 6]
]


for i in range(len(matrix)):
    temp_max = float('-inf')
    temp_min = float('inf')
    for j in range(len(matrix[i])):
        if matrix[i][j] > temp_max:
            temp_max = matrix[i][j]
        if matrix[i][j] < temp_min:
            temp_min = matrix[i][j]
    
    print("Max:",temp_max, end = " ")
    print("Min:",temp_min)