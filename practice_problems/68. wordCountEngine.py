from collections import OrderedDict
import string
def word_count_engine(document):
    docString = document.translate(str.maketrans('', '', string.punctuation))
    words = [word.lower() for word in docString.split()]
    count = OrderedDict()
    largestCount = 0
    for word in  words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
        largestCount = max(largestCount, count[word])

    counterList = [[] for _ in range(largestCount + 1)]
    for word, occurrence in count.items():
        counterList[occurrence].append([word, str(occurrence)])
    
    result = []
    for i in range(largestCount, -1, -1):
        for pair in counterList[i]:
            if pair:
                result.append(pair)
    return result

    
input_doc = "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"
print(word_count_engine(input_doc))