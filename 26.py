# Remove Duplicates from Sorted Array
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        p = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[p]: continue
            p += 1
            nums[p] = nums[i]
        return p + 1

s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))
print(nums)