class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        sp, ep = 0, 0
        count = 0
        while ep < len(s):
            if s[ep] in visited and sp <= visited[s[ep]]:
                sp = visited[s[ep]] + 1
            else:
                count = max(count, ep - sp + 1)
            visited[s[ep]] = ep
            ep += 1
        return count

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        count, start = 0, 0
        for end, letter in enumerate(s):
            if letter in visited and visited[letter] >= start:
                start = visited[letter] + 1
            else:
                count = max(count, end - start + 1)
            visited[letter] = end
        return count
  
# print(Solution().lengthOfLongestSubstring("hdcuwehfv hfcdnsjcnkj dhd kh jhfdjcjdhcjdhceuwhcadcknlndcen"))
# print(Solution().lengthOfLongestSubstring("abcabcbb"))
# print(Solution().lengthOfLongestSubstring("pwwkew"))
# print(Solution().lengthOfLongestSubstring(""))
print(Solution().lengthOfLongestSubstring("aab"))

