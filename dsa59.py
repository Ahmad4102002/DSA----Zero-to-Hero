# Problem: Check if Two Elements Exist with a Sum Equal to a Target Value

arr = [1,6,8,10]

target = 5

seen = set()

for each in arr:
    need = target - each
    if need in seen:
        print("FOUND")
    else:
        seen.add(each)


