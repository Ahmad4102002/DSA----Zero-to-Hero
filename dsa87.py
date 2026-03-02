# Add and Subtract Two Matrices

a= [
 [1, 2, 3],
 [4, 5, 6]
]

b = [
 [7, 8, 9],
 [1, 2, 3]
]

new = []
sub = []

# APPEND INTO NEW MATRIX 

for i in range(len(a)):
    new2 = []
    sub2 = []
    for j in range(len(a[i])):
        new2.append(a[i][j] + b[i][j])
        sub2.append(a[i][j] - b[i][j])
    new.append(new2)
    sub.append(sub2)
        
print(new)
print(sub)

