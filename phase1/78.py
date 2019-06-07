# Subsets
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
             return [[]]
        else:
            tmp = self.subsets(nums[1:])
            return [x + [nums[0]] for x in tmp] + tmp



if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))