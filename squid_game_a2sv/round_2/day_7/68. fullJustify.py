from typing import List


class Solution:
    # O(N * M) time and O(M) space, M = maxWidth
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
                elif token == "*":
                    spaceCount += 1
                else:
                    wordCount += 1
                    wordLen += len(token)
            # print("wl", wordLen, spaceCount, maxWidth - wordLen - spaceCount)
            if maxWidth - wordLen - spaceCount > 0:
                spaceCount += maxWidth - wordLen - spaceCount
            even, leftover = 1, 0
            if wordCount - 1 > 0:
                even, leftover = divmod(spaceCount, wordCount - 1)
            else:
                even, leftover = spaceCount, 0
            # print(even, leftover, res[i], spaceCount, wordCount - 1)
            rem = maxWidth
            for j, token in enumerate(res[i]):
                if token == "*":
                    res[i][j] = " " * (even)

            for j, token in enumerate(res[i]):
                if token.isspace() and leftover:
                    res[i][j] += " "
                    leftover -= 1

            rem -= sum(len(res[i][j]) for j in range(len(res[i])))
            # print(rem, res[i], len(res[i][0]))
            if rem > 0:
                res[i][0] = res[i][0] + (" " * rem)
            res[i] = "".join(res[i])

        rem = maxWidth
        for k, token in enumerate(res[-1]):
            # print(k, token, res[-1])
            if token == "*":
                res[-1][k] = " "

        rem -= sum(len(res[-1][j]) for j in range(len(res[-1])))
        print(rem, res[-1], k, token)

        # print(rem, "e", len("".join(res[-1])))
        if rem > 0:
            # print("and here", len(res[-1][0] + " "*rem))
            # print(res[-1], "nnnn")
            res[-1] += (" ")*rem
            # print(res[-1], "hhhh")
        res[-1] = "".join(res[-1])
        # print(len(res[-1]), maxWidth, len(res[-1].rstrip(" ")))
        if len(res[-1]) > maxWidth:
            res[-1] = res[-1].rstrip(" ")
        return res
