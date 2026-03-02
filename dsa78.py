# Generate All Possible Substrings of a String

s = "hello"

all = []

left = 0
n = len(s)
for i in range(n):
    sub = ""
    for j in range(i,n):
         
         sub += s[j]

         all.append(sub)


print(all)