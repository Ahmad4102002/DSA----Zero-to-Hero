n =int(input())

odd =[]
even = []
for i in range(n):
    num = int(input().strip())

    if num == 0:
        continue
    if num%2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(even)
print(odd)