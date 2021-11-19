def decodeSlantedCipher(s, rows):
    cols = len(s)//rows
    table = []
    sub = 0
    
    if cols == 0:
        return s
    for i in range(0, len(s), cols):
        table.append(list(s[i : i + cols]))
        sub = sub + cols

    ans = []
    for i in range(cols):
        if table[0][i]:
            ind = i
            for j in range(rows):
                if ind < cols:
                    ans.append(table[j][ind])
                    ind += 1
                else:
                    break
    return "".join(ans).rstrip()

s = "ch   ie   pr"
rows = 3

s = "iveo    eed   l te   olc"
rows = 4

s = "coding"
rows = 1

s =" b  ac"
rows = 2

s = ""
rows = 5
print(decodeSlantedCipher(s, rows))

