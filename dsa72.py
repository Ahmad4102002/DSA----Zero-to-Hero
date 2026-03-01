s = "helo"

# chekc if string contains two consecutive or 3 consecutive


n = len(s)


# save current element in saved 
# if next element is same as saved then count += 1 



#  if two then check fot three


for i in range(n-1):
    if s[i] == s[i+1]:
        print("FOUND")
        break
else:
    print("NOT FOUND")