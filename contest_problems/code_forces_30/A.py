for _ in range(int(input())):
    s = input()
    c = input()

    idx = [i for i in range(len(s)) if s[i] == c]
    print("YES" if any(i % 2 == 0 for i in idx) else "NO")