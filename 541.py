# Reverse String II
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        start, end = 0, k - 1
        while start < len(s):
            i, j = start, min(end, len(s) - 1)
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            start += 2*k
            end += 2*k
        return "".join(s)