class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        current = self.root
        word = word.lower()
        for char in word:
            key = ord(char) - ord('a')
            if not current.children[key]:
                current.children[key] = TrieNode()
            current = current.children[key]
        current.isEndOfWord = True

    def search(self, word, isPrefix = False):
        current = self.root
        word = word.lower()
        for char in word:
            key = ord(char) - ord('a')
            if not current.children[key]:
                return False
            current = current.children[key]
        return current.isEndOfWord or isPrefix

    def startsWith(self, prefix):
        return self.search(prefix, isPrefix = True)

    def delete(self, word):
        current = self.root
        path =[]
        for char in word:
            key = ord(char) - ord('a')
            if not current.children[key]:
                break
            path.append(current.children[key])
            current = current.children[key]
        else:
            if not path or path[-1].isEndOfWord != True:
                return
            for currentLayer, char in zip(path[:-1], reversed(word)):
                key = ord(char) - ord('a')
                if currentLayer.children[key]:
                    currentLayer.children[key] = None
                else:
                    break
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