# Sort Array By Parity II
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ans = [None] * len(A)
        p0 = 0
        p1 = 1
        for a in A:
            if a % 2 == 0:
                ans[p0] = a
                p0 += 2
            else:
                ans[p1] = a
                p1 += 2
        return ans

if __name__ == '__main__':
    a = [4,2,5,7]
    s = Solution()
    print(s.sortArrayByParityII(a))