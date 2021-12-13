from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, k = [[]], maxWidth
        for word in words:
            if k - len(word) >= 0:
                res[-1].append(word)
                k -= len(word)
                if k >= 0: 
                    res[-1].append("*")
                    k -= 1
            else:
                k = maxWidth
                res.append([word])
                k -= len(word)
                if k >= 0: 
                    res[-1].append("*")
                    k -= 1
        for i in range(len(res) - 1):
            wordCount, spaceCount, wordLen = 0, 0, 0
            for j, token in enumerate(res[i]):
                if j == len(res[i]) - 1 and token == "*":
                    res[i].pop()
                    spaceCount -= 1
                elif token == "*": spaceCount += 1
                else: 
                    wordCount += 1
                    wordLen += len(token)
            if maxWidth - wordLen - spaceCount > 0: spaceCount += maxWidth - wordLen - spaceCount
            even, leftover = 1, 0
            if wordCount - 1 > 0:
                even, leftover = divmod(spaceCount, wordCount - 1)
            else:
                even, leftover = spaceCount, 0
            rem = maxWidth
            for j, token in enumerate(res[i]):
                if token == "*":
                    res[i][j] = " " *(even)
            for j, token in enumerate(res[i]):
                if token.isspace() and leftover:
                    res[i][j] += " "
                    leftover -= 1         
            rem -= sum(len(res[i][j]) for j in range(len(res[i])))
            if rem > 0: res[i][0] = res[i][0] + (" " * rem)
            res[i] = "".join(res[i])
        rem = maxWidth
        for k, token in enumerate(res[-1]):
            if token == "*":
                res[-1][k] = " " 
        rem -= sum(len(res[-1][j]) for j in range(len(res[-1])))
        print(rem, res[-1], k, token)
        if rem > 0: 
            res[-1] += (" ")*rem
        res[-1] = "".join(res[-1])
        if len(res[-1]) > maxWidth: res[-1] = res[-1].rstrip(" ")
        return res

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(Solution().fullJustify(words, maxWidth))
