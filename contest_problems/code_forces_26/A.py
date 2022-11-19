n = int(input())
s = input().lower()
if n < 26:
    print("NO")
else:
    chars = set(list(s))
    if len(chars) < 26:
        print("NO")
    else:
        print("YES")