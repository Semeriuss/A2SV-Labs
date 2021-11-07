from collections import defaultdict, Counter
import heapq 
import string

def word_count_engine(document):
  docString = document.translate(string.maketrans("",""), string.punctuation)
  words = [word.lower() for word in docString.split()]

  wordMap = Counter(words)


  wordCount = []
  for word, order in wordMap.items():
    wordCount.append((order, word))
  
  heapq.heapify(wordCount)
  
  result = []
  while wordCount:
    result.append(heapq.heappop(wordCount))
  
  return result
  
 
  
    
  pass # your code goes here