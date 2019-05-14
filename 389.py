# Find the Difference
import collections

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = collections.Counter(s)
        for c in t:
            count[c] -= 1
        for a, b in count.items():
            if b == -1:
                return a
        return t


if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    sl = Solution()
    print(sl.findTheDifference(s, t))

