#  count the number of time 1 appers in ta list of numbers uptil n

n = 11

one_count = 0

for i in range(n+1):
    nex = i
    while nex > 0:
        digit = nex % 10
        
        if digit == 1:
            one_count += 1
        
        nex = nex // 10



print(one_count)
        