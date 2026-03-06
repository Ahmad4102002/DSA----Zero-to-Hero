a = 12 
b = 8 

sett = set() # will hold all common divisors 

for i in range(1,max(a,b)+1):
    if a % i == 0 and b % i == 0:
        sett.add(i)

gcd =max(sett)

if gcd == 1:
    print("Co prime")
else:
    print("not Co- Prime")