from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        current = self.root
        word = word.lower()
        for char in word:
            current = current.children[char]
        current.isEndOfWord = True
    
    def search(self, word, isPrefix = False):
        current = self.root
        word = word.lower()
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.isEndOfWord or isPrefix
    
    def startsWith(self, word):
        return self.search(word, isPrefix = True)

    def delete(self, word):
        current = self.root
        path = []
        for char in word:
            if char not in current.children:
                break
            path.append(current.children[char])
            current = current.children[char]
        
        if not path or path[-1].isEndOfWord == False:
            return
        
        for currentLayer, char in zip(path[:-1], reversed(word)):
            if currentLayer.children[char]:
                currentLayer.children.pop(char)
            else:
                return
        path[-1].isEndOfWord = False
        
trie = Trie()
words = ['There', 'The', 'Thermos', 'Their', 'Theirs']
for word in words:
    trie.addWord(word)
print(trie.search('THe'))
print(trie.startsWith('ther'))
trie.delete('the')
print(trie.search('THe'))
print(trie.startsWith('ther'))