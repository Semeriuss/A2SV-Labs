def sockMerchant(n, ar):

    sockSet = set()
    matchingPair = 0
    for sock in ar:
        if sock in sockSet:
            matchingPair += 1
            sockSet.remove(sock)
        else:
            sockSet.add(sock)
        
    return matchingPair

tests = [([1,2,1,2,1,3,2],7, 2)]
for test in tests:
    ar, n, expected = test
    actual = sockMerchant(n, ar)
    print(actual == expected, actual, expected)
        
