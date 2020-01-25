# Element Appearing More Than 25% In Sorted Array
from typing import List
import math

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        def binSearchLeft(n):
            nonlocal arr, l
            left, right = 0, l - 1
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= n:
                    right = mid
                elif left == mid:
                    return right
                else:
                    left = mid
            return left
        l = len(arr)
        mark = math.floor(l/4) + 1
        for i in range(1,4):
            num = arr[i * math.ceil(l/ 4) - 1]
            idx = binSearchLeft(num)
            if arr[idx + mark - 1] == num:
                return num
        return -1

s = Solution()
print(s.findSpecialInteger([1]))




