from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        possible_elements = [cardPoints[i - k] for i in range(k + 1)] 
        possible_elements.extend([cardPoints[i] for i in range(1, k)])
        n = len(possible_elements)

        startPointer = 0
        endPointer = k

        maxPoint = 0
        currMax = sum([possible_elements[0 + x] for x in range(k)])
        
        while endPointer < n:
            maxPoint = max(maxPoint, currMax)
            currMax -= possible_elements[startPointer]
            startPointer += 1
            currMax += possible_elements[endPointer]
            endPointer += 1
            
        maxPoint = max(maxPoint, currMax)
        
        return maxPoint



tests = [([2,2,2], 2), 
        ([1,2,3,4,5,6,1], 3), 
        ([9,7,7,9,7,7,9], 7), 
        ([1,1000,1], 1), 
        ([1,79,80,1,1,1,200,1], 3),
        ([96,90,41,82,39,74,64,50,30], 8)]

for test in tests:
    cardPoints, k = test
    print(Solution().maxScore(cardPoints, k))
