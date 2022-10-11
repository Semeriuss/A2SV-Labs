def solve(a, b):
    if a[-1] == b[-1]:
        if a[-1] == 'S':
            if len(a) > len(b):
                return '<'
            elif len(a) < len(b):
                return '>'
            else:
                return '='
        
        elif a[-1] == 'L':
            if len(a) > len(b):
                return '>'
            elif len(a) < len(b):
                return '<'
            else:
                return '='
        
        else:
            return '='
    
    else:
        if a[-1] == 'L':
            return '>'
        
        elif a[-1] == 'M':
            if b[-1] == 'L':
                return '<'
            else:
                return '>'

        else:
            return '<'

    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = input().split()
        print(solve(a, b))