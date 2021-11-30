def decrypt(word):
    ascii_vals = [ord(c) for c in word]
    ascii_diff = []
  
    if not word: return ''
    for i in range(1, len(ascii_vals)):
        ascii_diff.append(ascii_vals[i] - ascii_vals[i - 1])
        ascii_vals[0] -= 1
    
    for i in range(len(ascii_diff)):
        while ascii_diff[i] not in range(ord('a'), ord('z') + 1):
            ascii_diff[i] += 26
    
    res = [ascii_vals[0]] + ascii_diff
    return "".join(chr(ret) for ret in res)

