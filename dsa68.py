# Count vowels and consaontent in a strig

s = "programming"
vowels = set("aeiou")

count_vowels = 0
count_consonants = 0

for ch in s:
    if ch in vowels:
        count_vowels += 1
    else:
        count_consonants += 1

print(count_consonants - count_vowels)