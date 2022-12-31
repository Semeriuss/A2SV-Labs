from collections import Counter
s = input()

freq = Counter(list(s))
res = ""
for char, count in freq.items():
    palindrome = char*count
    if palindrome > res:
        res = palindrome

print(res)