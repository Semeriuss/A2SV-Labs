n = int(input())
a = list(map(int, input().split()))

if n < 6:
    print(n)
else:
    required = [4, 8, 15, 16, 23, 42]
    count = 0
    freq = {x : [0, []] for x in required}
    for i, num in enumerate(a):
        if num not in freq:
            count += 1
        else:
            freq[num][0] += 1
            freq[num][1].append(i)
    
    for v, indices in freq.values():
        indices.sort(reverse=True)

    VALID = True 
    sequences= 0
    while VALID:
        start_index = 0
        for num in required:
            count, indices = freq[num]
            if count == 0:
                VALID = False
                break 
            else:
                curr_index = freq[num][1].pop()
                freq[num][0] -= 1
                while freq[num][1] and curr_index < start_index:
                    curr_index = freq[num][1].pop()
                    freq[num][0] -= 1
                if curr_index < start_index:
                    VALID = False 
                    break 
                else:
                    start_index = curr_index
        
        if not VALID:
            break
        else:
            sequences += 1

    if sequences == 0:
        print(n)
    else:
        print(n - (sequences * 6))