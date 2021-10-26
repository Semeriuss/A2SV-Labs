import heapq
import bisect
from typing import List

class Solution:
    def lastStoneWeight2(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            bisect.insort(stones, stones.pop() - stones.pop())
        return stones[0] if len(stones) == 1 else 0
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        
        while len(stones) > 0:
            if len(stones) == 1:
                break
            max1 = heapq._heappop_max(stones)
            max2 = heapq._heappop_max(stones)
            if max1 == max2:
                continue
            else:
                heapq.heappush(stones, abs(max1 - max2))
                heapq._heapify_max(stones)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0

stones = [2,7,4,1,8,1] 
stones = [1]


stones = [4,5,2,7,6]
     
print(Solution().lastStoneWeight(stones))
print(Solution().lastStoneWeight2(stones))