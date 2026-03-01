# Count the Number of Words in a String

s = " Hello   World  Python  bastard bitch"


i = 0

n = len(s)
count = 0 

while i < n and s[i] == " ":
    i += 1 



# when " " is seen increase count to +1

while i < n:
    if s[i] == " ":
        count += 1 
        while i < n and s[i] == " ":
            i += 1
    i += 1

print(count)
