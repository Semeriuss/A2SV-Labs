from collections import defaultdict
import heapq
animals = []
players = []
ROW, COL = len(animals), len(animals[0])
print(ROW)
print(COL)
scoreMap = defaultdict(int)
for col in range(COL):
    # col = 0
    currentColumn = [animals[col][row] for row in range(ROW)]
    heap = []
    for i, value in enumerate(currentColumn):
        heapq.heappush(heap, (value, players[i]))
    
    start = 1
    while heap:
        score, player = heapq.heappop(heap)  
        scoreMap[player] += start 
        start += 1
    
    # col += 1

print(scoreMap)