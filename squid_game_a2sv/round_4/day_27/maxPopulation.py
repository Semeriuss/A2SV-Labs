class Solution:
    # O(N) time and space
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        res = 0
        count = defaultdict(int)
        for b, d in logs:
            count[b] += 1
            count[d] -= 1

        for i in range(1950, 2051):
            count[i] += count[i - 1]
            res = res if count[res] >= count[i] else i

        return res
