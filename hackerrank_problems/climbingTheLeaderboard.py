import heapq
def climbingLeaderboard(ranked, player):
    
    heap = []
    current = None
    current_rank = 1
    prev = None
    for rank in ranked:
        current = rank
        if prev == current: continue
        heapq.heappush(heap, (current, current_rank))
        current_rank += 1
        prev = current
    
    print(heap)
    res = []
    playerscore, rank = heapq.heappop(heap)
    for p in player:
        print(rank, playerscore)
        if p > playerscore:
            while heap and p > playerscore:
                playerscore, rank = heapq.heappop(heap)

        if p == playerscore: res.append(rank)
        elif p > playerscore: res.append(1)
        else: res.append(rank + 1)
    
    return res
        
ranked = [100, 90, 90, 80]
player = [70, 80, 105]

ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]

ranked = [100, 90, 90, 80, 75, 60]
player = [50, 65, 77, 90, 102]
print(climbingLeaderboard(ranked, player))