# Check if a number is an armstrong number

n = 1534

original = n
digit_count= 0 
new_sum = 0 

while n > 0:
    digit_count += 1
    n = n // 10

n = original

while n > 0:
    digit = n % 10
    new_sum = new_sum + digit **digit_count
    n = n //10

if new_sum == original:
    print("Armstrong Number")
else:
    print("Not Armstong number")