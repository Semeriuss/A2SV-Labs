def areNumbersAscending(s):
    """
    :type s: str
    :rtype: bool
    """
    sentence = s.split()
    
    currentNum = float("-inf")

    for token in sentence:
        if token.isdigit() and float(token) <= currentNum:
            return False
        elif token.isdigit():
            currentNum = float(token)
    return True


s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
s = "hello world 5 x 5"
s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
s = "4 5 11 26"
print(areNumbersAscending(s))

        