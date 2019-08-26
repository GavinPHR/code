# Find All Duplicates in an Array
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            if nums[abs(x) - 1] < 0: ans.append(abs(x))
            else: nums[abs(x) - 1] *= -1
        return ans

s = Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1]))