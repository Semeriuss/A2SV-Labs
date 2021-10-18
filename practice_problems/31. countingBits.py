from math import log

def countingBits(n):
    store = [0]
    count = 0
    for i in range(1, n+1):
        if i%2 != 0:
            count += 1
        if log(i, 2).is_integer():
            count = 1
        if not log(i,2).is_integer() and i%4 == 0:
            count = 2
        store.append(count)

    return store
###

def countingBits(n):
    memo = [0 for i in range(n+1)]
    return countBits(memo, n)

def countBits(memo, n):
    if n == 0:
        return 0

    if n < 3:
        return 1
    
    if log(n, 2).is_integer():
        return 1

    if not log(n,2).is_integer() and n%4 == 0:
        return 2
    
    if memo[n]:
        return memo[n]

    memo[n] = countBits(memo, n-1) + countBits(memo, n-2)
    return memo[n]
###

#BruteForce
def toListOfBin(n):
    return list(str(bin(n)))
def oneBits(n):
    return toListOfBin(n).count("1")
def countingBits(n):
    store = []
    for i in range(n+1):
        store.append(oneBits(i))
    return store

#Oneliner (bruteforce)
def countingBits(n):
    return [list(str(bin(i))).count("1") for i in range(n+1)]


def countingBits(num):
    bit_count = {0:0, 1:1}
    ans = []

    for number in range(num+1):
        count = 0
        n = number
        while n:
            if n in bit_count:
                break
            else:
                count += (n &1)
                n = n >> 1
        bit_count[number] = bit_count[n] + count
        ans.append(bit_count[number] + count)

    return ans

    

    
print(countingBits(10))
