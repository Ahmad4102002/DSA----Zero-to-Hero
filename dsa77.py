# Find a Specific Substring within a String

s = "hello worl  world"
sub ="world"

# start loop form w

# fixed sliding window of length sub 

bub = "world"



k = len(sub)
# build string of length sub 

# first build the first string 
left = 0
for right in range(len(s)):
    result = ""  
    while (right - left + 1 > k):   # when to move left ------- when -- right - left > k (len of sub):
        left += 1 
                                # build i new string
    for each in range(left,right+1):
        result += s[each]
    
    if result == sub:
        print("FOUND", left)
        break 




        
