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

# custom test case
# for n in range(2, 20):
#     print(primeSumsOf(n))

print(primeSumsOf(n))