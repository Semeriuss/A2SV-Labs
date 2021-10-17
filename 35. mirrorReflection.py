def mirrorReflection(p, q):
    k = 1
    while(k*q%p): k += 1
    
    if k%2 == 0 and (k*q//p)%2 == 1: return 2
    if k%2 == 1 and (k*q//p)%2 == 1: return 1
    if k%2 == 1 and (k*q//p)%2 == 0: return 0

tests = [((3,2), 0), ((4,3),2)]
for test in tests:
    given, expected = test
    p, q = given
    actual = mirrorReflection(p, q)
    print(actual == expected, actual, expected)
