# Find the Number of Trailing Zeroes in the Factorial of a Given Number n
n = 100
factorial = 1
for i in range(n,0,-1):

    factorial = factorial * i 



original = factorial 
count = 0
while (original > 0):
    digit = original % 10

    if digit == 0:
        count +=1 
    else:
        break 
    original = original // 10

print(count)