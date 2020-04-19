class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            n = None
            if (nums[mid] < nums[0]) == (target < nums[0]):
                n = nums[mid]
            else:
                n = -float('inf') if target < nums[0] else float('inf')
            if target < n:
                r = mid - 1
            elif target > n:
                l = mid + 1
            else:
                return mid
        return -1
            
                
                
        
        
        