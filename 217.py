# Contains Duplicate
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1,2,3]))