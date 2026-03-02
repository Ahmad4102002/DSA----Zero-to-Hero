# remove first character and last character and k th character

s = "hello"

result = ""
k = 2 
# run loop over s add into new string skip first 


for i in range(len(s)):
    if i == 0 or i == len(s)-1 or i == k-1 :
        continue
    else:   
        result += s[i]

print(result)