numberOfDorms, numberOfLetters = tuple(list(map(int, input().split())))
dorms = list(map(int, input().split()))
letters = list(map(int, input().split()))

def findDorms(dorms, letters):

    prefixDorms = [0]
    for i in range(len(dorms)):
        prefixDorms.append(dorms[i] + prefixDorms[-1])
    
    dormNumber = 1
    letterNumber = 0
    while dormNumber < len(prefixDorms) and letterNumber < len(letters):
        if letters[letterNumber] <= prefixDorms[dormNumber]:
            print(dormNumber, letters[letterNumber] - prefixDorms[dormNumber - 1])
            letterNumber += 1
        
        else:
            dormNumber += 1

findDorms(dorms, letters)
