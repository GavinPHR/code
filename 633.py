# Sum of Square Numbers
import math
class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c))+1):
            print(i)
            if math.sqrt(c - i**2) % 1 < 0.001:
                return True
        return False

s = Solution()
print(s.judgeSquareSum(999999999))