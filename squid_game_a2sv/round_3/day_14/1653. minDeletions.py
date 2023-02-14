class Solution:
    # O(N) time and space
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        aCount = bCount = 0
        arr = []
        for c in s:
            if c == 'a':
                aCount += 1
            else:
                bCount += 1
            arr.append((aCount, bCount))
        if not bCount or not aCount:
            return 0
        count = n
        for i, c in enumerate(s):
            count = min(count, arr[i][1] - int(c == 'b') + aCount - arr[i][0])

        return count
