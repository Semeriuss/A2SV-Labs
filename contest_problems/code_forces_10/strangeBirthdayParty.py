
import heapq

def findMinimumCost(friends, presents):
    heapq._heapify_max(friends)
    cost = 0
    currentPresent = 0
    
    while friends:
        currentFriend = heapq._heappop_max(friends)
        if currentPresent < len(presents) and currentPresent <= presents[currentPresent]:
            cost += min(presents[currentPresent], presents[currentFriend - 1])
            currentPresent += 1
        else:
            cost += presents[currentFriend - 1]
    
    return cost

if __name__ == "__main__":
    t = int(input())
    res = []
    for i in range(t):
        n, m = list(map(int, input().split()))
        friends = list(map(int, input().split()))
        presents = list(map(int, input().split()))
        res.append(findMinimumCost(friends, presents))
    print(*res, sep="\n")
    