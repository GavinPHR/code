# Move Zeroes
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p] = nums[i]
                p += 1
        while p != len(nums):
            nums[p] = 0
            p += 1
        return

if __name__ == '__main__':
    a = [0,1,0,3,12]
    s = Solution()
    s.moveZeroes(a)
    print(a)