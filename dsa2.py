# first line 4 space 
# next line 4 spaces - 1 

for j in range(4):
    print(" ")
    for k in range(4-j):
        print(" ", end = " ")
    for i in range(4):
        print("*", end = " ")