s = "abcabcbb"

sett = set()

# loop on s ---- expand and add into set until already in set 
# if already in set then - left 

left = 0 

max_length = float('-inf')

for right in range(len(s)):
     # if a is already in set 
        while s[right] in sett:                # i have to decrease the windwo till 
                                           # the required alphabet has left 
            sett.remove(s[left])
            left += 1

        sett.add(s[right])     
        
        length = right - left + 1 
        max_length= max(max_length,length)

print(max_length)