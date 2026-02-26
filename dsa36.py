n = 5
         # 1 2 3 4 5
for i in range(n):          #V start
    for j in range(i,-1,-1): # 1 ,     start from i go back(-1) till 0(-1)
        print(j+1,end="")
    print()