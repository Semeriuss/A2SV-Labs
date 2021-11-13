
import heapq
def makeProductEqualOne(nums):

    evenNegativesCase = 0
    oddNegativesCase = []
    zeroCount = 0

    negativeCount = 0

    cost = 0
    for num in nums:
        if num > 0:
            cost += abs(num - 1)
        elif num < 0:
            negativeCount += 1
            evenNegativesCase += abs(num + 1)
            heapq.heappush(oddNegativesCase, num)
        else:
            zeroCount += 1

    if negativeCount % 2 == 0:
        cost += zeroCount
        return cost + evenNegativesCase

    while len(oddNegativesCase) > 1:
        cost += abs(heapq.heappop(oddNegativesCase) + 1)
    
    finalNegative = heapq.heappop(oddNegativesCase)
    if zeroCount > 0:
        cost += 1
        cost += abs(finalNegative + 1)
        zeroCount -= 1
    else:
        cost += abs(finalNegative - 1)

    cost += zeroCount

    return cost

# tests = [[-1, 1], [0,0,0,0], [-5, -3, 5, 3, 0], [-4, -5, -3, 5, 3, 0]]
# for test in tests:
#     print(makeProductEqualOne(test))

# test = [-1, 3, 0]
# print(makeProductEqualOne(test))

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(makeProductEqualOne(nums))
