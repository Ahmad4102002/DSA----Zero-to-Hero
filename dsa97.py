# Reverse a Given Number

i = 978

total = 0

while i > 0:
    digit = i % 10
    total = total * 10 + digit
    i = i // 10

print(total)