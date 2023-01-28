def and_list(X):
    # We initialize our result to 1 as initalizing to
    # the result to 0 coupled with an AND logic would
    # absorb every value.
    res = 1
    for num in X:
        # Continuously calculating AND logic
        # between values consecutively.
        res &= num

    return res


def xor_list(X):
    # We initialize our result to 0 so as not to lose a
    # single bit due to an XOR operation as same values
    # give 0 in XOR logic.
    res = 0
    for num in X:
        # Continuously calculating XOR logic
        # between values consecutively.
        res ^= num

    return res

# Assertions
# X = [3, 5, 1]
# print(and_list(X) == 1)
# print(xor_list(X) == 7)


# Helper Function to retrive all sublists
# of a list.
def getSublist(A):
    sublists = [[val] for val in A]
    n = len(A)
    for i in range(n - 1):
        temp = [A[i]]
        for j in range(i + 1, n):
            temp.append(A[j])
            sublists.append(temp[:])
    return sublists

# Helper function test
# print(getSublist([3, 5, 1]))


def f(X):
    if X == []:
        return 0

    sublists = getSublist(X)
    xor_vals = []

    # Retrieving XOR
    for sublist in sublists:
        # Appending the XOR value of each sublist
        # (using xor_list function defined previously)
        xor_vals.append(xor_list(sublist))

    # Calculating the AND of the XOR values
    res = and_list(xor_vals)

    return res


# Assertion
# print(f([3, 5, 1]) == 0)

def f_eff(X):
    if X == []:
        return 0
    # Appending the XOR value of each value in the list
    # (using xor_list function defined previously)
    xor_val = xor_list(X)

    # Calculating the AND of the XOR values
    if xor_val == 0:
        return 1
    else:
        return 0


# Assertion
print(f_eff([3, 5, 1]))
