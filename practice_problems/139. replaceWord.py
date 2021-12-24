from typing import List
       
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        def replace(word):
            for i in range(len(word)):
                if word[:i] in roots: return word[:i]
            return word
        return " ".join(map(replace, sentence.split()))
                


dictionary = ["cat", "bat", "rat"]
sentence = "The cat was rattled by the battle"
print(Solution().replaceWords(dictionary, sentence))

        