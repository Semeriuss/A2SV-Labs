from math import sqrt
import sys

input = sys.stdin.readline
n = int(input())

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def primeSumsOf(n): 
    primes = [i for i in range(2, n) if isPrime(i)]
    primeSum = set()
    for prime in primes:
        if prime in primeSum:
            return f'{prime} {n - prime}'
        primeSum.add(n - prime)
    return -1

def primeSumsOf(n):
    primeSum = set([2])
    for num in range(2, n):
        if isPrime(num) and isPrime(n - num) and num in primeSum:
            return f'{num} {n - num}'
        primeSum.add(n - num)
    return -1

# sieve of erasthones
def sieveOfErasthones(n):
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False

    p = 2
    while p*p <= n:
        if(primes[p]):
            for j in range(p**2, n+1, p):
                primes[j] = False
        p += 1
    return primes

def primeSumOf(n):
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False
    primeSum = set([i for i in range(n + 1)])
    p = 2
    while p*p <= n:
        if(primes[p]):
            for j in range(p**2, n+1, p):
                primes[j] = False
        p += 1

    return primes
    

    

## custom test case
# for n in range(2, 20):
#     print(n, primeSumsOf(n))

print(primeSumsOf(n))
