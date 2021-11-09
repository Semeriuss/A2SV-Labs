def maxSubArraySum(red, blue):

    currMax = 0
    currVal = 0
    
    commonIndex = min(len(red), len(blue))
    leftOver = max(len(red), len(blue))

    lastIndex = 0
    for i in range(commonIndex):
        currVal += max(red[i], blue[i])
        currMax = max(currVal, currMax)
        currVal += min(red[i], blue[i])
        lastIndex = i
        
    
    if lastIndex + 1 < len(red):
        for j in range(lastIndex + 1, leftOver):
            currVal += red[j]
            currMax = max(currVal, currMax)
    
    elif lastIndex + 1 < len(blue):
        for j in range(lastIndex + 1, leftOver):
            currVal += blue[j]
            currMax = max(currVal, currMax)
    
    return currMax

if __name__ == "__main__":
    t = int(input())

    tests = []
    res = []
    for i in range(t):
        n = int(input())
        red = list(map(int, input().split()))

        m = int(input())
        blue = list(map(int, input().split()))
        res.append(maxSubArraySum(red, blue))

    print(*res, sep="\n")
