class Solution:
    def minimumBuckets(self, street: str) -> int:
        N = len(street)

        i = 0
        minBuckets = 0
        visited = set()
        while i < N:
            if i > 0 and i < N - 1:
                if street[i] == 'H':
                    if street[i - 1] != '.' and street[i + 1] != '.':
                        return -1
                    elif street[i - 1] != '.':
                        return -1
                    elif street[i + 1] != '.':
                        minBuckets += 1
                        i += 2
                    else:
                        minBuckets += 1
                        i += 1
                else:
                    if street[i - 1] == '.' and i - 1 not in visited:
                        i += 1
                    elif street[i + 1] == '.':
                        visited.add(i)
                        minBuckets += 1
                        i += 1
                    else:
                        minBuckets += 1
                        i += 2
            
            else:
                i += 1
        return minBuckets

street = "H..H"
street = ".H.H."
print(Solution().minimumBuckets(street))