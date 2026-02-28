s = "  Hello   World     Python "

arr = []

result = ""

for each in s:
    if each == " ":
        print()
    else:
        result += each

print(result)

