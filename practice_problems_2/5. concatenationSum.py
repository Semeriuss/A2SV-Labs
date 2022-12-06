def concatenationsSum(a):
    return (sum(10**digit_length(n) for n in a) + len(a)) * sum(a)


def digit_length(n):
    return len(str(n))

print(concatenationsSum([10, 2]))