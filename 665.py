# Non-decreasing Array
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 2: return True
        found = False
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]: continue
            if found: return False
            if i - 2 >= 0:
                if nums[i] >= nums[i - 2]:
                    found = True
                    continue
                else:
                    nums[i] = nums[i - 1]
            else:
                m = min(nums[0], nums[1])
                nums[0], nums[1] = m, m
            found = True
        return True


s = Solution()
print(s.checkPossibility([1,5,4,6,7,10,8,9]))