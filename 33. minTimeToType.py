def minTimeToType(word):
    currentChar = 'a'
    timer = 0
    offset = 0

    for char in word:
        timer += min([abs(ord(char) - ord(currentChar)), abs((ord(char.upper()) + 6) - ord(currentChar)), abs(ord(char) - (ord(currentChar.upper()) + 6))]) + 1
        currentChar = char#char.upper() if abs((ord(char.upper()) + 6) - ord(currentChar)) < abs(ord(char) - ord(currentChar)) else char.lower()
    return timer


tests = [("abc", 5), ("bza", 7), ("zjpc", 34)]
for test in tests:
    word, expectedTime = test
    actualTime = minTimeToType(word)
    print(actualTime == expectedTime, actualTime, expectedTime)
    
