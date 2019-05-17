# Prime Number of Set Bits in Binary Representation
from typing import List


class Solution:
    PRIME = {2,3,5,7,11,13,17,19,23,29,31}
    def countPrimeSetBits(self, L: int, R: int) -> int:
        ans = 0
        for i in range(L, R + 1):
            count = 0
            for j in bin(i)[2:]:
                if int(j) == 1:
                    count += 1
            if count in self.PRIME:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimeSetBits(248657,257888))