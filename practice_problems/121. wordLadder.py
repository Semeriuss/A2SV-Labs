from collections import defaultdict, deque
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                generic = word[:i] + '_' + word[i+1:]
                graph[generic].append(word)

        que, visited = deque([(beginWord, 1)]), set([beginWord])
        while que:
            for _ in range(len(que)):
                word, count = que.popleft()
                if word == endWord: return count
                for i in range(len(word)):
                    generic = word[:i] + '_' + word[i+1:]
                    if generic in graph:
                        for possibleWord in graph[generic]:
                            if possibleWord not in visited:
                                que.append((possibleWord, count + 1))
                                visited.add(possibleWord)
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog","hog"]

# beginWord = "hiu"
# endWord = "cog"
# wordList = ["hut","dot","dog","lot","log","hog","cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))

