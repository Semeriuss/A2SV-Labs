import sys 

input = sys.stdin.readline

probabilities = list(map(int, input().split()))
smallRPoint, zanoesPoint = (probabilities[0], probabilities[1]), (probabilities[2], probabilities[3])
def archer(sP, zP):
    a, b = sP
    c, d = zP

    smallRProbability = a/b
    zanoesProbability = c/d
    losingProbability = (1 - smallRProbability) * (1 - zanoesProbability)

    return smallRProbability * (1/ (1 - losingProbability))

print(archer(smallRPoint, zanoesPoint))    