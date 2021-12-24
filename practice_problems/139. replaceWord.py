from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()  
        current = root
        for word in dictionary:
            for c in word:
                if c not in current.children: current.children[c] = TrieNode()
                current = current.children[c] 
            current.isEndOfWord = True
            current = root
        
        words = sentence.split(" ")
        res = ""
        for word in words:
            index = self.startsAt(root, word)
            if index:
                res += word[:index - 1]
            else:
                res += word
            res += " "
        return res.rstrip(" ")
    
    def startsAt(self, root: TrieNode, prefix: str) -> int:
        current = root
        for i, c in enumerate(prefix):
            if current.isEndOfWord: return i + 1
            if c not in current.children: return 0
            current = current.children[c]
        return 0
            
        