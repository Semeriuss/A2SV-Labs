

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N = len(s)

        t_dict = Counter(t)
        s_dict = defaultdict(int)

        def matches(t, s):
            for x in t:
                if s[x] < t[x]:
                    return False
            return True

        start, end = 0, 0
        res = ""
        while start <= end and end < N:

            if matches (t_dict, s_dict):
                res = s[start : end + 1] if len(s[start : end + 1]) < len(res) or len(res) < len(t) else res
                if s[start] in t_dict: s_dict[s[start]] -= 1
                start += 1
            
            elif s[end] in t_dict:
                s_dict[s[end]] += 1
                if matches(t_dict, s_dict):
                    res = s[start : end + 1] if len(s[start : end + 1]) < len(res) or len(res) < len(t) else res
                
                if end < N - 1:
                    end += 1
                else: 
                    start += 1
            
            else:
                end += 1
        
        return res