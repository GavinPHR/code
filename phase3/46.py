# Permutations
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        ans = []
        s = set(nums)
        for i in range(len(nums)):
            scopy = s.copy()
            scopy.remove(nums[i])
            print(s)
            rec = [[nums[i]]+p for p in self.permute(list(scopy))]
            ans += rec
        return ans

s = Solution()
print(s.permute([1,2,3]))
