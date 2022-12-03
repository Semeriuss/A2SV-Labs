n = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if n == 0:
    print(0)
else:
    resA = 0
    for c in a:
        resA |= c
    resB = 0
    for c in b:
        resB |= c
    print(resA + resB)