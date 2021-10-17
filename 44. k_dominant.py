import sys


input = sys.stdin.readline
s = input()
inputChars = list(s[:len(s)])

print(inputChars)
    
def minKDominant(listOfChars):
    
    n = len(listOfChars)  
    hashmap = {}
    for i, char in enumerate(listOfChars):
        if char in hashmap:
            return i - hashmap[char]
        else:
            hashmap[char] = i
    
    return n//2 + 1 if n % 2 != 0 else n//2


def minKDominant(listOfChars):
    
    k = float("inf")
    n = len(listOfChars)
    
    for i in range(26):
        letter = chr(ord('a') + i)
        start = end = currentK = 0
        while end < n:
            if letter == listOfChars[end]:
                currentK = max(currentK, end - start + 1)
                start = end 
            end += 1
        currentK = max(currentK, end - start)
        k = min(currentK, k)
    return k

def minKDominant(inputChars):
    n = len(inputChars)
    k = n

    for pos in range(26):
        letter = chr(ord('a') + pos)
        currentk = last_occurence = 0
        for i, char in enumerate(inputChars):
            if letter == char:
                currentk = max(currentk, i - last_occurence)
                last_occurence = i
        currentk = max(currentk, n - last_occurence)
        k = min(currentk, k)
    return k

print(minKDominant(inputChars))