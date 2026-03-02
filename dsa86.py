# Find the Maximum and Minimum Values in Each Column of a Matrix

matrix = [
 [3, 5, 1],
 [7, 2, 8],
 [4, 9, 6]
]


for i in range(len(matrix)):
    temp_max = float('-inf')
    temp_min = float('inf')
    for j in range(len(matrix[i])):
        if matrix[j][i] > temp_max:
            temp_max = matrix[j][i]
        if matrix[j][i] < temp_min:
            temp_min = matrix[j][i]
    
    print("Max:",temp_max, end = " ")
    print("Min:",temp_min)