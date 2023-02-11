for _ in range(int(input())):
    n = int(input())
    s = input()
    if n < 2:
        print(n)
    else:
        start, end = 0, n - 1
        if s[start] == s[end]:
            print(n)
        else:
            while start < end and s[start] != s[end]:
                start += 1
                end -= 1
            print(end - start + 1)
