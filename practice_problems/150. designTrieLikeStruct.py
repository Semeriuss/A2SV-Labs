class WordDictionary:
    
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        current = self.trie
        for c in word:
            if c not in current: current[c] = {}
            current = current[c]   
        current['#'] = {}
     
    def searchR(self, part: str, trie: dict) -> bool:
        current = trie
        exists = False
        for i, c in enumerate(part):
            if c == ".": 
                for s in current:
                    if self.searchR(part[i+1:], current[s]): return True
            if c not in current: return False
            current = current[c]
        return "#" in current
    
    def search(self, word: str) -> bool:
        current = self.trie
        for i, c in enumerate(word):
            if c == ".":
                for s in current:
                    if self.searchR(word[i+1:], current[s]): return True
                return False
            if c not in current: return False
            current = current[c]
        return "#" in current


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)