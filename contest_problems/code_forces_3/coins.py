import sys

input = sys.stdin.readline
conditions = []
for i in range(3):
    conditions.append(input())

def coins(conditions):
    
    coin_state = {'A': 0, 'B': 0, 'C': 0}

    for condition in conditions:
        if condition[1] == '>':
            if condition[0] == 'A':
                coin_state['A'] += 1
            elif condition[0] == 'B':
                coin_state['B'] += 1
            elif condition[0] == 'C':
                coin_state['C'] += 1

        elif condition[1] == '<':
            if condition[2] == 'A':
                coin_state['A'] += 1
            elif condition[2] == 'B':
                coin_state['B'] += 1
            elif condition[2] == 'C':
                coin_state['C'] += 1

    order = ["", "", ""]
    IMPOSSIBLE = False
    prev_value = float('-Inf')
    for k, v in coin_state.items():
        if prev_value == v:
            IMPOSSIBLE = True
            break
        prev_value = v
        order[v] = k
    
    if not IMPOSSIBLE:
        print("".join(order))
    else:
        print("Impossible")

coins(conditions)
        