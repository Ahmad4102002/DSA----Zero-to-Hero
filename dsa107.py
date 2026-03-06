# recursion and factorial

n = 6

# 10 * 9 


def factorial(n):   # keep th enumber alive by passing through recursion 
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(n))