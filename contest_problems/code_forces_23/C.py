def solve(l, r, a):
    if a == 1:
        return r
    if r % a == 0:
        if l == r:
            return r//a 
        else:
            return (r - 1)//a + (r - 1)%a 
    else:
        possible = (r//a)*a - 1 
        if possible >= l:
            return max(r//a + r%a, possible//a + possible%a)
        else:
            return r//a + r%a 

for _ in range(int(input())):
    l, r, a = map(int, input().split())
    print(solve(l, r, a))