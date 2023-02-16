class Solution:
    # O(N) time and space
    def romanToInt(self, s: str) -> int:
        mapper = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        res = 0
        i = 0
        n = len(s)
        while i < n - 1:
            if s[i] == 'I':
                if s[i + 1] == 'V' or s[i + 1] == 'X':
                    res += mapper[s[i + 1]] - 1
                    i += 2
                else:
                    res += 1
                    i += 1
            elif s[i] == 'X':
                if s[i + 1] == 'L' or s[i + 1] == 'C':
                    res += mapper[s[i + 1]] - 10
                    i += 2
                else:
                    res += mapper[s[i]]
                    i += 1
            elif s[i] == 'C':
                if s[i + 1] == 'D' or s[i + 1] == 'M':
                    res += mapper[s[i + 1]] - 100
                    i += 2
                else:
                    res += mapper[s[i]]
                    i += 1
            else:
                res += mapper[s[i]]
                i += 1
        if i == n - 1:
            res += mapper[s[i]]
        return res
