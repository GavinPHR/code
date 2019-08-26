# Continuous Subarray Sum
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: return False
        cumsum = (nums[0] + nums[1]) % k if k != 0 else nums[0] + nums[1]
        if cumsum == 0: return True
        s = set()
        s.add(nums[0] % k if k != 0 else nums[0])
        buffer = cumsum
        for i in range(2, len(nums)):
            cumsum = (cumsum + nums[i]) % k if k != 0 else cumsum + nums[i]
            if cumsum in s or cumsum == 0: return True
            s.add(buffer)
            buffer = cumsum
        return False

s = Solution()
print(s.checkSubarraySum([0, 1, 0, 0], 0))