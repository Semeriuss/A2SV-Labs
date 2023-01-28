def successor(A):
    res = []
    # A flag to notify whether the value has been incremented.
    succeeded = False
    for num in A:
        if not succeeded:
            # This means this trit is at its max capacity,
            # and hence must transfer its value as a carry.
            if num == 2:
                res.append(0)

            # Here we can simply increment the value at the
            # least trit position.
            else:
                res.append(num + 1)
                succeeded = True

        # If the value has already been incremented,
        # we just append the remaining trits.
        else:
            res.append(num)

    # Finally, we check if a carry value has been transferred
    # outside the bounds of the loop as in the case for [2,2,2]
    # in which case we add a 1 at the next higher trit position
    # making this example -> [0, 0, 0, 1].
    if not succeeded:
        res.append(1)

    return res


# Assertions
# print(successor([2, 2, 1]) == [0, 0, 2])
# print(successor([2, 2, 2]) == [0, 0, 0, 1])
# print(successor([]) == [1])


def leq(A, B):
    # Making the list sizes equal for convenience.
    if len(A) < len(B):
        A += [0] * (len(B) - len(A))
    elif len(B) < len(A):
        B += [0] * (len(A) - len(B))

    n = len(B)

    # We start from the most significant digits and
    # return at the earliest difference observed.
    for i in range(n - 1, -1, -1):
        if A[i] < B[i]:
            return True
        elif A[i] > B[i]:
            return False
    return True


# Assertions
# print(leq([2, 0, 1], [0, 1, 1]) == True)
# print(leq([2, 0, 1, 0], [2, 0, 1]) == True)
# print(leq([0, 1, 1], [2, 0, 1]) == False)


def tritwise_min(A, B):

    # Making the list sizes equal for convenience.
    if len(A) < len(B):
        A += [0] * (len(B) - len(A))
    elif len(B) < len(A):
        B += [0] * (len(A) - len(B))

    res = []

    # Iterate at each trit position and pick the minimum value.
    for a, b in zip(A, B):
        res.append(min(a, b))

    # Nit: Removing leading zeroes from the list (not necessary).
    while res and res[-1] == 0:
        res.pop()

    return res


# Assertions
# print(tritwise_min([1, 0, 2], [1, 1, 1]) == [1, 0, 1])
# print(tritwise_min([2, 1], [0, 2, 1]) == [0, 1])
# print(tritwise_min([2, 0, 1], [0, 1, 1]) == [0, 0, 1])
# print(tritwise_min([0, 1, 1], [1, 1, 1]) == [0, 1, 1])


def f(A, B):

    # Convenince: equating the list sizes
    if len(A) < len(B):
        A += [0] * (len(B) - len(A))
    elif len(B) < len(A):
        B += [0] * (len(A) - len(B))

    res = A
    A = successor(A)

    # Main condition for the function: increment until A reaches B
    while leq(A, B):
        res = tritwise_min(res, A)
        A = successor(A)
    return res

# Assertions
# print(f([2, 0, 1], [1, 1, 1]) == [0, 0, 1])


def f_eff(A, B):
    if len(A) < len(B):
        A += [0] * (len(B) - len(A))
    elif len(B) < len(A):
        B += [0] * (len(A) - len(B))
    n = len(A)

    res = []

    # We just need to compare the trit positions at A and B
    # and pick the trit value based on the position.
    for i in range(n - 1, -1, -1):
        a, b = A[i], B[i]
        if a > b:
            res.append(0)
        elif a < b:
            res.append(a)
        else:
            res.append(a)
    return res[::-1]


print(f_eff([2, 0, 1], [1, 1, 1]) == [0, 0, 1])
