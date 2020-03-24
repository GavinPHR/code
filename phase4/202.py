# Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            n = sum(int(c)**2 for c in str(n))
            if n in s: return False
            # print(n)
            if n == 1: return True
            s.add(n)
        return False

s = Solution()
print(s.isHappy(19))

