global prefix
global suffix

def helper(left, right, string, dp = {}, prefix="", suffix=""):
    if left > right:
        return ""

    elif left == right and string[left] == string[right]:
        prefix += string[left]
        return "" + helper(left+1, right-1, string, dp, prefix, suffix)

    elif string[left] == string[right]:
        helper(left+1, right-1, string, dp, prefix, suffix)
    else:
        helper(left+1, right, string, dp, prefix, suffix)
        helper(left, right-1, string, dp, prefix, suffix)

def palindrome(string):
    return 