class Solution:
    # O(N*M) time and O(M) space
    def validIPAddress(self, queryIP: str) -> str:
        parts = queryIP.split(':')
        parts = queryIP.split('.') if parts[0] == queryIP else parts
        hexa = set(['A', 'B', 'C', 'D', 'E', 'F',
                   'a', 'b', 'c', 'd', 'e', 'f'])
        if len(parts) == 4:
            for part in parts:
                for c in part:
                    if not c.isdigit():
                        return "Neither"
                if not part or (len(part) != 1 and part[0] == '0') or not (0 <= int(part) <= 255):
                    return "Neither"
            return "IPv4"
        elif len(parts) == 8:
            for part in parts:
                for c in part:
                    if not c.isdigit() and not c in hexa:
                        return "Neither"
                if not part or len(part) > 4:
                    return "Neither"
            return "IPv6"
        else:
            return "Neither"
