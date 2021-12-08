from collections import deque
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        target = list(endWord)
        
        if endWord not in wordSet: return 0
        
        foundPath = False
        visited = set()
        finalCount = 0

        que = deque([(list(beginWord), 0)])
        visited.add(beginWord)
        
        while que:
            word, count = que.popleft()
            
            for i in range(len(word)):
                tmp = word[i]
                for letter in range(ord('a'), ord('z') + 1):
                    word[i] = chr(letter)
                    permutedWord = "".join(word)
                    if permutedWord not in visited and permutedWord in wordSet:
                        if not foundPath:
                            count += 1
                        foundPath = True
                        visited.add(permutedWord)
                        if word == target: 
                            finalCount = count + 1
                            return finalCount 
                            
                        que.append((word.copy(), count))
                word[i] = tmp
            if foundPath: 
                count += 1
                foundPath = False
        return finalCount
                
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog","hog"]

beginWord = "hiu"
endWord = "cog"
wordList = ["hut","dot","dog","lot","log","hog","cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))

