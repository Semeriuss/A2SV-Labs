class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        sp, ep = 0, 0
        count = 0
        while ep < len(s):
            print(sp, ep, count, s[sp], s[ep], s)
            print(visited)
            if s[ep] in visited and sp <= visited[s[ep]]:
                sp = visited[s[ep]]
            else:
                count = max(count, ep - sp)
            visited[s[ep]] = ep
            ep += 1
        count = max(count, ep - sp)
        return count
    
print(Solution().lengthOfLongestSubstring("hdcuwehfv hfcdnsjcnkj dhd kh jhfdjcjdhcjdhceuwhcadcknlndcen"))