from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        trie = {}

        for word in wordDict:
            current = trie
            for c in word:
                current = current.setdefault(c, {})
            current['#'] = True
        

        leads = [trie]
        for i, char in enumerate(s):
            new_leads = []
            trie_added = False
            while leads:
                lead = leads.pop()
                if char not in lead: continue
                lead = lead[char]
                new_leads.append(lead)
                if '#' in lead and not trie_added:
                    new_leads.append(trie)
                    trie_added = True
            leads = new_leads
        
        return trie in leads

s = "leetCode"
wordDict = ["leet", "Code"]
print(Solution().wordBreak(s, wordDict))    