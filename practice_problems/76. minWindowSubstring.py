from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        N = len(s)
        
        if not s or not t or len(t) > N: return ''
        
        t_count = Counter(t)
        s_count = Counter()
        
        t_chars = len(t_count)
        matching_chars = 0
        
        start, end = 0, -1
        res = ''
        while start < N:
            
            if matching_chars < t_chars:
                if end == N - 1: return res
                end += 1
                s_count[s[end]] += 1
                if t_count[s[end]] > 0 and s_count[s[end]] == t_count[s[end]]:
                    matching_chars += 1
                    
            else:
                s_count[s[start]] -= 1
                if t_count[s[start]] > 0 and s_count[s[start]] == t_count[s[start]] - 1:
                    matching_chars -= 1
                start += 1
            
            if matching_chars == t_chars:
                if not res:
                    res = s[start : end + 1]
                else:
                    if end - start + 1 < len(res):
                        res = s[start : end + 1]
        return res
                
        
        