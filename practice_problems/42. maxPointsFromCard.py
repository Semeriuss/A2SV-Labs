from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        possible_indices = [i - k for i in range(k + 1)] 
        possible_indices.extend([i for i in range(1, k)])
        n = len(possible_indices)

        maxPoint = 0
        for i in range(n - k + 1):
            maxPoint = max(maxPoint, sum([cardPoints[possible_indices[i + x]] for x in range(k)]))
        return maxPoint

# ([2,2,2], 2), 
#         ([1,2,3,4,5,6,1], 3), 
#         ([9,7,7,9,7,7,9], 7), 
#         ([1,1000,1], 1), 
#         ([1,79,80,1,1,1,200,1], 3),

tests = [
        ([96,90,41,82,39,74,64,50,30], 8)]

for test in tests:
    cardPoints, k = test
    print(Solution().maxScore(cardPoints, k))
