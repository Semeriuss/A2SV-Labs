class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.isEndOfWord = True

    def search(self, word: str, isPrefix: bool = False) -> bool:
        current = self.root
        for c in word:
            if c not in word: return False
            current = current.children[c]
        return current.isEndOfWord or isPrefix

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)