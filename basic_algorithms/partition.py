from typing import List


def partition(s: str) -> List[str]:
    if len(s) > 0:
        for p in range(len(s)):
            prefix, suffix = s[:p+1], s[p+1:]
            for part in partition(suffix):
                yield [prefix] + part
    else:
        yield []

print(*partition("1234"))
    