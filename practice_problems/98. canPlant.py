from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        slots, i, length = 0, 0, len(flowerbed)
        while i < length:
            if flowerbed[i] or (i - 1 >= 0 and flowerbed[i - 1]) or (i + 1 < length and flowerbed[i + 1]):
                i += 1
            else:
                slots += 1
                i += 2
            if slots == n:
                break
        return slots == n

flowerbed = [1,0,0,0,1]
n = 2

flowerbed = [0]
n = 1

# flowerbed = []
# n = 9

flowerbed = [1,0,0,0,0,1]
n = 2
print(Solution().canPlaceFlowers(flowerbed, n))