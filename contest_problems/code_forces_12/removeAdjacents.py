def removeAdjacent(s):
    
    stack = []
    count = 0
    curr = None
    for i in range(len(s)):
        print(curr, stack, count)
        if curr and abs(ord(s[curr]) - ord(s[i])) == 1:
            count += 1
            curr += 1
        if stack and abs(ord(stack[-1]) - ord(s[i])) == 1:
            curr = len(stack) - 1 if ord(stack[-1]) < ord(s[i]) else i
            stack.append(s[i])
            count += 1
        else:
            stack.append(s[i])

    return count

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(removeAdjacent(s))