class Solution:
    def minimumBuckets(self, street: str) -> int:
        N = len(street)

        i = 0
        minBuckets = 0
        visited = set()
        while i < N:
            if i in visited or i - 1 in visited or i + 1 in visited:
                    i += 1
                    continue
            if i > 0 and i < N - 1:
                if street[i] == 'H' and street[i - 1] == 'H' and street[i + 1] == 'H':
                    return -1
                elif street[i] == 'H' and street[i - 1] == 'H' and street[i + 1] == '.':
                    visited.add(i)
                    minBuckets += 1
                    i += 3
                if street[i] == 'H' and street[i - 1] == '.' and street[i + 1] == 'H':
                    visited.add(i)
                    minBuckets += 1
                    i += 1
                elif street[i] == 'H' and street[i - 1] == '.' and street[i + 1] == '.':
                    visited.add(i)
                    minBuckets += 1
                    i += 3
                elif street[i] == '.' and street[i - 1] == 'H' and street[i + 1] == 'H':
                    visited.add(i + 1)
                    minBuckets += 1
                    i += 3
                elif street[i] == '.' and street[i - 1] == 'H' and street[i + 1] == '.':
                    visited.add(i)
                    minBuckets += 1
                    i += 2
                elif street[i] == '.' and street[i - 1] == '.' and street[i + 1] == 'H':
                    i += 1
                elif street[i] == '.' and street[i - 1] == '.' and street[i + 1] == '.':
                    i += 1
                else:
                    i += 1
            elif i == 0:
                if street[i] == 'H' and i + 1 < N and street[i + 1] == 'H':
                    return -1
                elif street[i] == 'H' and i + 1 < N and street[i + 1] == '.':
                    visited.add(i)
                    minBuckets += 1
                    i += 2
                elif street[i] == 'H' and i + 1 >= N:
                    return -1
                elif street[i] == '.' and street[i + 1] == 'H':
                    visited.add(i + 1)
                    minBuckets += 1
                    # print("hi")
                    i += 3 if  i + 3 < N else 2
                else:
                    i += 1
            elif i == N - 1:
                if street[i] == 'H' and i - 1 > 0 and street[i - 1] == 'H':
                    return -1
                elif street[i] == 'H' and i - 1 > 0 and street[i - 1] == '.':
                    visited.add(i)
                    minBuckets += 1
                    i += 1
                else:
                    i += 1
            print(i - 1, i, i + 1, minBuckets)
        return minBuckets

street = "H..H"
street = ".H.H."
street = ".HHH."
street = "H"
street = "."
street = ".HH.H.H.H.."
print(Solution().minimumBuckets(street))