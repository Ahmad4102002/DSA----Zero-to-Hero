"""
Input: dummy_input = ["Hello","World"]

Output: ["Hello","World"]

"""

input = ["Hello","World"]

def encode(input : list[str]) -> str: # encode it into 5#Hello5#World
    result = ""

    for each in input:
        result += str(len(each)) + "#" + each
    
    return result # 5#Hello5#world

def decode(s: str) -> list[str]:
    
    i = 0
    n = len(s) 
    liss = []
    while i < n:
        res =""
        j = i 
        while s[j] != "#":
            j += 1 

        num = int(s[i:j])    

        res += s[j+1:j+1+num]

        liss.append(res)

        i = j + num + 1 

    print(liss)

decode("5#Hello5#world")

