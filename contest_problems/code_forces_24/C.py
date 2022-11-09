import heapq
n = int(input())
row = list(map(int, input().split()))
passengers = input()
heap = []
for i, r in enumerate(row):
    heapq.heappush(heap, (r, i + 1))

res = []
forExtroverts = []
for p in passengers:
    if p == "0":
        nextAvailableSeat, index = heapq.heappop(heap)
        res.append(index)
        forExtroverts.append(index)
    else:
        res.append(forExtroverts.pop())
print(*res)

