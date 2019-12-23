# Burst Balloons
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def p(d):
            for row in d:
                print(row)
        nums = [1] + [x for x in nums if x != 0] + [1]
        l = len(nums)
        if l == 2: return 0
        dp = [[0] * l for _ in range(l)]
        for k in range(0, len(nums) - 2):
            for i in range(1, len(nums) - 1 - k):
                j = i + k
                for m in range(i,j+1):
                    dp[i][j] = max(dp[i][j], dp[i][m-1] + dp[m + 1][j] + nums[m] * nums[i - 1] * nums[j + 1])
                    p(dp)
                    print()

        return dp[1][-2]




s = Solution()
print(s.maxCoins([3,1,5,8]))
# 167