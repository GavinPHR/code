# Peak Index in a Mountain Array
from typing import List

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        idx = 0
        for i in range(1, len(A)):
            if A[i] < A[idx]:
                return idx
            else:
                idx = i
        return -1
    
if __name__ == '__main__':
    a = [0, 2, 1, 0]
    s = Solution()
    print(s.peakIndexInMountainArray(a))