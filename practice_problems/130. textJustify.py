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

        for j, line in enumerate(res):
            space, words = 0, 0
            for i, token in enumerate(line):
                # print(i, len(line)-1, token, line, j)
                print(res[len(res) - 1])
                # if i == len(line) - 1 and token == "*": 
                #     line[i] = ""
                #     space += 1
                if token == "*": space += 1
                else: words += len(token)
            
            wordCount = len(line) - space - 1
            if maxWidth - words - space > 0: space += maxWidth - words - space
            print(space, wordCount, line, maxWidth - words - space)
            even, leftover = 1, 0
            if wordCount >= 0: 
                if wordCount == 0: wordCount = 1
                even, leftover = divmod(space, wordCount)
                print(even, leftover)
            print("space", space, "word")
            
            if j == len(res) - 1:
                first, last = True, True
                rem = maxWidth
                for i, token in enumerate(line):
                    if first and token == "*":
                        line[i] = " "
                        rem -= 1
                        first = False
                    elif i == len(line) - 1:
                        line[i] = " " * rem
                    elif token == "*":
                        line[i] = " "
                    else:
                        rem -= len(token)
                
            else:
                first = True
                for i, token in enumerate(line):
                    print(line, even, leftover, i)
                    if first and token == '*':
                        line[i] = " " * (even + leftover)
                        first = False
                    elif token == '*':
                        line[i] = " " * even  
                print(line)
            res[j] = "".join(line)
            print(len(res[j]))
            
        return res
                

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(Solution().fullJustify(words, maxWidth))
