from collections import defaultdict, Counter, OrderedDict
import collections
import string


def word_count_engine(document):

    docString = document.translate(str.maketrans('', '', string.punctuation))
    words = [word.lower() for word in docString.split()]

    result = sorted([list(t) for t in Counter(words).items()], key=lambda x: (-x[1], words.index(x[0])))
  
    for i in range(len(result)):
        result[i][1] = str(result[i][1])
    return result

    
input_doc = "Practice makes perfect, you'll get perfecT by practice. just practice! just just just!!"
print(word_count_engine(input_doc))