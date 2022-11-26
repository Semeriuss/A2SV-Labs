n, s = map(int, input().split())
forward = list(map(int, input().split()))
reverse = list(map(int, input().split()))

turns = [i for i, open in enumerate(forward) if open]
rTurns = [i for i, open in enumerate(reverse) if open]

if 1 == s:
    print("YES")

elif not forward[0]:
    print("NO")

else:
    if s - 1 in turns:
        print("YES")
    else:
        if s - 1 not in rTurns:
            print("NO")
        else:
            VALID = False
            for turn in turns:
                if turn >= (s - 1) and reverse[turn]:
                    VALID = True
                    break 
            
            print("YES") if VALID else print("NO")
