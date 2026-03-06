# ["Hello","World"]
# i will put delimiter in between 


"""
def encode(strs: list[str]) -> str:
    new = ""
    for each in strs:
        for letter in each:
            new += letter
        new += "_"
    return new 

def decode(s: str) -> list[str]:
    liss =[]
    new = ""
    for i in range(len(s)):
        if s[i] == "_":
            liss.append(new)
            new = ""
        else:
            new += s[i] 

    return liss



sex = ["Hello","World"]
print(encode(sex))

print(decode("Hello_World_"))

"""




# input = ["Hello","World"]
# output =  #5Hello#5World


def encode(strs: list[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
        
    print(res)

# input = 5#Hello5#World
# output = ["Hello","World"]

def decode(s: str) -> list[str]: #  5#Hello5#World
    res = []

    i = 0 
    n = len(s)

    while i < n:
        result = ""
        if s[i] == "#":
            num = int(s[i-1])
            i += 1 
            while num > 0 :
                result += s[i]

                i += 1
                num -= 1
            res.append(result)
        else:
            i += 1
    return res

print(decode("5#Hello5#World"))


