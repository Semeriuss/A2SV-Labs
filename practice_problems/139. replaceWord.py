import collections
from typing import List
       
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        _trie = lambda: collections.defaultdict(_trie) 
        root = _trie()
        
        END = True
        for word in dictionary:
            current = root
            for c in word:
                if c not in current: current[c] = _trie()
                current = current[c] 
            current[END] = word
        
        def replace(word):
            current = root
            for c in word:
                if c not in current: break
                current = current[c]
                if END in current: return current[END]
            return word
        
        return " ".join(map(replace, sentence.split()))
                


dictionary = ["cat", "bat", "rat"]
sentence = "The cat was rattled by the battle"
print(Solution().replaceWords(dictionary, sentence))

        