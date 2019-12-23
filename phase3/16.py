# 3Sum Closest
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[-1]
        for i in range(len(nums) - 2):
            l, m, r = i, i + 1, len(nums) - 1
            while m < r:
                tmp = nums[l] + nums[m] + nums[r]
                if abs(target - tmp) < abs(target - ans):
                    ans = tmp
                if tmp > target:
                    r -= 1
                else:
                    m += 1
        return ans

        # one, two, three = set(), set(), set()
        # for n in nums:
        #     for i in two:
        #         three.add(n + i)
        #     for i in one:
        #         two.add(n + i)
        #     one.add(n)
        # diff = float('inf')
        # ans = 0
        # for n in three:
        #     tmp = abs(target - n)
        #     if tmp < diff:
        #         ans = n
        #         diff = tmp
        # return ans

s = Solution()
print(s.threeSumClosest([1,1,-1,-1,3], 1))