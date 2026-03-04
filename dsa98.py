# check if a number is a palindrome


n = 1221

original = n 

new = 0

while n > 0:
    digit = n % 10 
    new = new*10 + digit
    n = n // 10 

if original == new:
    print("Palindrome")
else:
    print("Not Palindrome")