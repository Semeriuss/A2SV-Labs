class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        sp, ep = 0, 0
        count = 0
        print(len(s))
        while ep < len(s):
            if s[ep] in visited:
                count = max(count, ep - sp)
                visited.remove(s[sp])
                sp += 1
            else:
                visited.add(s[ep])
                ep += 1
        count = max(count, ep - sp)
        return count
    
print(Solution().lengthOfLongestSubstring(" "))