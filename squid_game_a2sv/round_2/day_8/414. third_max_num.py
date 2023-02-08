from typing import List
import heapq


class Solution:
    # O(N) time and space -> Can be improved to O(1) space by using three variables
    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        maxNum = 0
        seen = set()
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            maxNum = max(num, maxNum)
            if len(heap) == 3:
                heapq.heappushpop(heap, num)
            else:
                heapq.heappush(heap, num)
        return heapq.heappop(heap) if len(heap) == 3 else maxNum
