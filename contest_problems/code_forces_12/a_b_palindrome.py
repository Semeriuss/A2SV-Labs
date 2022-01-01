from collections import deque

def makePalindrome(a, b, s):

    sp, ep = 0, len(s) - 1
    for char in s:
        if char == "0":
            a -= 1
        elif char == "1":
            b -= 1

    leftEnd = []
    rightEnd = deque()
    while sp < ep:
        print(leftEnd, rightEnd, a, b)
        if s[sp] == s[ep] == "?":
            if a%2 == 0 and a > 1:
                a -= 2
                rightEnd.appendleft("0")
                leftEnd.append("0")
            
            elif b%2 == 0 and b > 1:
                print("hi")
                b -= 2
                rightEnd.appendleft("1")
                leftEnd.append("1")
            
            else:
                if a > 1:
                    a -= 2
                    rightEnd.appendleft("0")
                    leftEnd.append("0")
                
                elif b > 1:
                    b -= 2
                    rightEnd.appendleft("1")
                    leftEnd.append("1")
                
                else:
                    return -1 

        elif s[sp] == "?" and s[ep] != "?":
            if s[ep] == "1":
                if b >= 1:
                    b -= 1
                    rightEnd.appendleft("1")
                    leftEnd.append("1")
                
                else:
                    return -1
            
            elif s[ep] == "0":
                if a >= 1:
                    a -= 1
                    rightEnd.appendleft("0")
                    leftEnd.append("0")
                
                else:
                    return -1
        
        elif s[ep] == "?" and s[sp] != "?":
            if s[sp] == "1":
                if b >= 1:
                    b -= 1
                    rightEnd.appendleft("1")
                    leftEnd.append("1")
                
                else:
                    return -1
            
            elif s[sp] == "0":
                if a >= 1:
                    a -= 1
                    rightEnd.appendleft("0")
                    leftEnd.append("0")
                
                else:
                    return -1
        
        else:
            if s[sp] == s[ep]:
                leftEnd.append(s[sp])
                rightEnd.appendleft(s[ep])
            else:
                return -1
        print(leftEnd, rightEnd, a, b)
        sp += 1
        ep -= 1
    
    else:
        if sp == ep and s[ep] == "?":
            if a == 1:
                a -= 1
                leftEnd.append("0")
            
            elif b == 1:
                b -= 1
                leftEnd.append("1")            
            else:
                return -1
        
        else:
            # print(s[sp], s[ep], sp, ep)
            print(len(leftEnd) + len(rightEnd), len(list(s)), "lennn")
            if len(leftEnd) + len(rightEnd) < len(list(s)):
                if s[sp] != "?":
                    leftEnd.append(s[sp])
                
                else:
                    if a > 0:
                        leftEnd.append("0")
                        a -= 1
                    elif b > 0:
                        leftEnd.append("1")
                        b -= 1
                    else:
                        return -1
                    

    print(leftEnd, rightEnd, a, b)
    leftEnd.extend(rightEnd)
    return "".join(leftEnd) if a == b == 0 else -1

if __name__ == "__main__":
    t = int(input())
    res = []
    for _ in range(t):
        a, b = map(int, input().split())
        s = input()
        res.append(makePalindrome(a, b, s))
    
    print(*res, sep="\n")


# 5 4
# ??????0??
# 010101010