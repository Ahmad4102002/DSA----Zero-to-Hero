i = 96


total = 0 



while i > 0:
    digit = i % 10
    total += digit
    i = i // 10 


print(total)
