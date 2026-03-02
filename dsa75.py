# Insert a Character at the First, Last, and Kth Position in a String

# String: "hello"
# Character: "X"
# k = 2


# insert at first


s = "hello"
x = "X"


k = 2 

result = ""
last_result = ""
n_result = ""


result += x
for i in range(len(s)):
    result += s[i]
    
print(result)



for i in range(len(s)):
    last_result += s[i]
last_result += x

print(last_result)

for i in range(len(s)):
    if i == k:
        n_result += x
    n_result += s[i]

print(n_result)

