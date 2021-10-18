import sys


input = sys.stdin.readline
s = input()
inputString = s
    
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

def minKDominant(inputString):
    n = len(inputString)
    k = n

    # abb
    # currentK = 2, 
    for pos in range(26):
        letter = chr(ord('a') + pos)
        currentk = 0
        last_occurence = -1

        #i = 0,  char = a, letter = b
        for i, char in enumerate(inputString):
            if letter == char:
                currentk = max(currentk, i - last_occurence)

                #lastOccurence = 0,  
                last_occurence = i

        currentk = max(currentk, n - last_occurence)

        #k = 2
        k = min(currentk, k)
    return k

def minKDominant(inputString):
    n = len(inputString.split()[0])
    k = n
 
    for pos in range(26):
        letter = chr(ord('a') + pos)
        currentk = 0
        last_occurence = -1
        for i, char in enumerate(inputString):
            if letter == char:
                currentk = max(currentk, i - last_occurence)
                last_occurence = i
                print(currentk, last_occurence, n)
        currentk = max(currentk, n - last_occurence)
        k = min(currentk, k)
    return k
 
print(minKDominant(inputString))