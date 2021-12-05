class Solution:
    def minimumBuckets(self, street: str) -> int:
        street = "H" + street + "H"
        N = len(street)
        lastBucketIndex = -1
        minBuckets = 0
        for i in range(1, N - 1):
            if street[i] == 'H' and lastBucketIndex != i - 1:
                if street[i + 1] == '.':
                    lastBucketIndex = i + 1
                    minBuckets += 1
                elif street[i - 1] == '.':
                    lastBucketIndex = i - 1
                    minBuckets += 1
                else:
                    return -1       
        return minBuckets 


street = "H..H"
street = ".H.H."
street = ".HHH."
street = "H"
street = "."
street = ".HH.H.H.H.."
print(Solution().minimumBuckets(street))