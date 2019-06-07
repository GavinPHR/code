# N-Repeated Element in Size 2N Array
from typing import List

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        B = []
        for i in A:
            if i in B:
                return i
            else:
                B.append(i)
        return -1

if __name__ == '__main__':
    A = [5,1,5,2,5,3,5,4]
    s = Solution()
    print(s.repeatedNTimes(A))