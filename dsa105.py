n = 9

# find all factors 
# if factor count is 2 and 2nd factor  !=  7 then break
count = 0 

for i in range(1,n+1):
    if n % i == 0:
        if i != 1 and i != n:
            print("Not Prime")
            break
else:
    print("Prime")