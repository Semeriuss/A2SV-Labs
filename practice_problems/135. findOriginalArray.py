from typing import List
from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        numCount = Counter(changed)
        if numCount[0] % 2: return []
        for num in sorted(numCount):
            if numCount[num] > numCount[num * 2]: return []
            numCount[num * 2] -= numCount[num] if num else numCount[num]//2
        return list(numCount.elements())