# First Bad Version

def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n
        if isBadVersion(1): return 1
        while True:
            mid = (l + r) // 2
            if isBadVersion(mid): r = mid
            else: l = mid
            if r - l == 1: return r

s = Solution()
print(s.firstBadVersion(15))