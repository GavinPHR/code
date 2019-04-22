# Self Dividing Numbers
from typing import List

class Solution:
    def isTrue(self, x: int) -> bool:
        xx = x
        digits = []
        while xx != 0:
            digits.append(xx%10)
            xx = xx//10
        if 0 in digits: return False
        for d in digits:
            if x%d != 0: return False
        return True
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [x for x in range(left,right+1) if self.isTrue(x)]

if __name__ == '__main__':
    s = Solution()
    print(s.selfDividingNumbers(1,22))