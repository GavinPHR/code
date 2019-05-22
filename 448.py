# Find All Numbers Disappeared in an Array
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = [False] * len(nums)
        for i in nums:
            seen[i - 1] = True
        return [i + 1 for i in range(len(nums)) if seen[i] != True]

if __name__ == '__main__':
    a = [1,2,3]
    s = Solution()
    print(s.findDisappearedNumbers(a))