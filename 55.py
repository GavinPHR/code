class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ = 0
        for i, n in enumerate(nums):
            if i > max_:
                return False
            if i + n > max_:
                max_ = i + n
        return True
            