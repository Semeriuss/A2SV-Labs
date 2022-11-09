for _ in range(int(input())):

    s = input()
    start, end = ord(s[0]) - ord('a'), ord(s[-1]) - ord('a') 
    cost = abs(end - start) 
    mapper = [(c, i + 2) for i, c in enumerate(s[1:-1]) if min(start, end) <= ord(c) - ord('a') <= max(start, end)]
    mapper.sort(reverse = True if start > end else False)
    res = [1] + [i for _, i in mapper] + [len(s)]
    print(cost, len(res))
    print(*res)
