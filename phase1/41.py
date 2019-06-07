# First Missing Positive
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        nums.append(0)
        def partition(l, r):
            p = nums[r]
            i, j = l - 1, r + 1
            while i < j:
                while True:
                    j -= 1
                    if nums[j] <= p:
                        break
                while True:
                    i += 1
                    if nums[i] >= p:
                        break
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            return j
        l = partition(0, len(nums) - 1) + 1
        nums = sorted(nums[l:])
        print(nums)
        acc = 1
        for n in nums:
            if n != acc:
                if n == acc - 1:
                    continue
                return acc
            acc += 1
        return acc



if __name__ == '__main__':
    n = [0,2,2,1,1]
    s = Solution()
    print(s.firstMissingPositive(n))
