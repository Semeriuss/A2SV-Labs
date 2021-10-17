import sys

input = sys.stdin.readline
nAndk = tuple(list( map(int, input().split())))
n, k = nAndk

input = sys.stdin.readline
fullSet = list( map(int, input().split()))
    
def maxKMultipleFreeSet(originalSet, givenK):
    hashSet = set(originalSet)

    for element in originalSet:
        product =  element*givenK
        if product in hashSet:
            hashSet.remove(element)
    
    return len(hashSet)

def maxKMultipleFreeSet(originalList, givenK):
    maxSet = set()
    originalList.sort()
    for element in originalList:
        if element/givenK not in maxSet:
            maxSet.add(element)
    return len(maxSet)

print(maxKMultipleFreeSet(fullSet, k))