class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i, n in enumerate(nums):
            ans[i] = nums[i] * (ans[i-1] if i > 0 else 1)
        r = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = r * (ans[i - 1] if i > 0 else 1)
            r *= nums[i]
        return ans