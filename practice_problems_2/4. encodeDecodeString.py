class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = []
        for string in strs:
            res.append(str(len(string)))
            res.append(string)
        return "".join(res)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        i = 0
        res = []
        while i < len(str):
            res.append(str[i + 1 : i + 1 + int(str[i])])
            i += int(str[i]) + 1
        return res


s = Solution()
arr = ["we", "say", ":", "yes"]
arr = ["lint","code","love","you"]
arr = ["%", ":", ";", "hi", " ", "-"]
arr = ["hey", "4", "you"]
encoded = s.encode(arr)
decoded = s.decode(encoded)
print(decoded)