from collections import deque
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(sp, md, ep):
            ans = deque(s[md])
            while sp >= 0 and ep < len(s):
                if s[sp] == s[ep]:
                    ans.append(s[ep])
                    ans.appendleft(s[sp])
                    ep += 1
                    sp -= 1                
                else:
                    break
            if sp == md - 1 and s[sp] == s[md]:
                ans.appendleft(s[sp])
            elif ep == md + 1 and s[ep] == s[md]:
                ans.append(s[ep])
            else:
                ans = deque(s[md])
            return "".join(ans)
        
        ans = ""
        for i in range(1, len(s) - 1):
            md = i 
            sp = md - 1
            ep = md + 1
            res = getPalindrome(sp, md, ep)
            ans = res if len(res) >= len(ans) else ans
        return ans


s = "babad"
# s= "cbbd"
s = "a"
s = "ac"
def isPalindrome(s, sp, ep):
    while sp < ep:
        if s[sp] != s[ep]:
            return False
        sp += 1
        ep -= 1
    return True

def getPalindrome(s, sp, ep, sub): 
    if sp < 0 and ep >= len(s):
        return ""   
    if isPalindrome(s, sp, ep):
        return isPalindrome(s, sp - 1, ep) or isPalindrome(s, sp, ep + 1) or isPalindrome(s, sp - 1, ep + 1)
    
    sub = res if len(res) >= len(ans) else ans




print(Solution().longestPalindrome(s))
