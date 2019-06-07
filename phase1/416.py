# Partition Equal Subset Sum
from typing import List


class Solution:
    # must be even
    # only need to find one partition of sum = sum(nums) / 2
    # ->> coin denom problem
    def canPartition(self, nums: List[int]) -> bool:
        def recur(amount, m):
            if amount < 0 or m < 0:
                return False
            if amount == 0:
                return True
            return recur(amount - nums[m], m - 1) or recur(amount, m - 1)
        s = sum(nums)
        if s % 2 != 0:
            return False
        psize = s / 2
        nums.sort()
        if nums[-1] > psize:
            return False
        return recur(psize, len(nums) - 1)


if __name__ == '__main__':
    a= [2, 2, 3, 5]
    s = Solution()
    print(s.canPartition(a))
    print(a)