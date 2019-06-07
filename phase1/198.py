# House Robber
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 4:
            if N == 1:
                return nums[0]
            if N == 2:
                return max(nums)
            if N == 3:
                return max(nums[0] + nums[2], nums[1])
        dp = [nums[0], nums[1], nums[0] + nums[2]]
        for i in range(3, N):
            dp.append(nums[i] + max(dp[i - 3], dp[i - 2]))
        return max(dp[-2], dp[-1])


if __name__ == '__main__':
    s = Solution()
    print(s.rob([1,2,3,1]))
