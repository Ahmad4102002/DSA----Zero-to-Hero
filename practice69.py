s = "   Hello    World   Python   "

result = ""

i = 0 
n = len(s)

while i < n and s[i] == " ":
    i += 1

while i < n:
    if s[i] != " ":
        result += s[i]
    else:
        result += " "
        while i < n and s[i] == " ":
            i += 1
        continue
    i += 1 

if len(result) > 0 and result[-1] == " ":
    result = result [:-1]
print(len(result))
