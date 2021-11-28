def moveZerosToEnd(arr):
    output = []
    zero_count = 0
    for num in arr:
        if num == 0:
            zero_count += 1
        else:
            output.append(num)
        if zero_count != 0:
            output.extend([0 for _ in range(zero_count)])
    return output