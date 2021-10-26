from math import sqrt
import sys

input = sys.stdin.readline
n = int(input()) # n is assumed to be a prime number

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def primeSumsOf(n):
    return f'2 {n-2}' if isPrime(n-2) else -1


print(primeSumsOf(n))
