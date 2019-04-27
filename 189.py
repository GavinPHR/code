# Rotate Array
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            nums.insert(0, nums.pop())

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7]
    k = 3
    s = Solution()
    s.rotate(a, k)
    print(a)
