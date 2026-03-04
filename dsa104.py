# GCD greatest common divisor GCD(12, 8) = 4


# check all the common divisrs

a = 12 
b = 8 

sett = set() # will hold all common divisors 

for i in range(1,max(a,b)+1):
    if a % i == 0 and b % i == 0:
        sett.add(i)

gcd =max(sett)

lcm = (a * b) / gcd

    