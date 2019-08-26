# First Unique Character in a String
import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        d = collections.Counter(s)
        i = 0
        for c in s:
            if d[c] == 1:
                return i
            else:
                i += 1
        return -1



s = Solution()
print(s.firstUniqChar("loveleetcode"))

