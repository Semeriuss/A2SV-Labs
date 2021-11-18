from collections import deque

def makePalindrome(a, b, s):

    sp, ep = 0, len(s) - 1
    
    palindrome = deque()
    leftEnd = []
    rightEnd = []
    while sp < ep:
        print(palindrome)
        if s[sp] == s[ep] == "?":
            if a > 1:
                a -= 2
                palindrome.append("0")
                palindrome.appendleft("0")
            
            elif b > 1:
                b -= 2
                palindrome.append("1")
                palindrome.appendleft("1")
            
            else:
                return -1 

        elif s[sp] == "?" and s[ep] != "?":
            if s[ep] == "1":
                if b > 1:
                    b -= 2
                    palindrome.append("1")
                    palindrome.appendleft("1")
                
                else:
                    return -1
            
            elif s[ep] == "0":
                if a > 1:
                    a -= 2
                    palindrome.append("0")
                    palindrome.appendleft("0")
                
                else:
                    return -1
        
        elif s[ep] == "?" and s[sp] != "?":
            if s[sp] == "1":
                if b > 1:
                    b -= 2
                    palindrome.append("1")
                    palindrome.appendleft("1")
                
                else:
                    return -1
            
            elif s[sp] == "0":
                if a > 1:
                    a -= 2
                    palindrome.append("0")
                    palindrome.appendleft("0")
                
                else:
                    return -1
        
        else:
            if s[sp] == s[ep]:
                leftEnd.append(s[sp])
                rightEnd.append(s[ep])
            else:
                return -1
                
        print(palindrome)
        sp += 1
        ep -= 1
    
    else:
        if sp == ep and s[ep] == "?":
            if a == 1:
                a -= 1
                palindrome.append("0")
            
            elif b == 1:
                b -= 1
                palindrome.append("1")            
            else:
                return -1

    # leftEnd.extend(palindrome)
    # leftEnd.extend(rightEnd)
    # print(leftEnd)
    print(leftEnd, rightEnd)
    palindrome.extendleft(leftEnd)
    palindrome.extend(rightEnd)
    return "".join(palindrome)

if __name__ == "__main__":
    t = int(input())
    res = []
    for _ in range(t):
        a, b = map(int, input().split())
        s = input()
        res.append(makePalindrome(a, b, s))
    
    print(*res, sep="\n")


