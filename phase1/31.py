# Next Permutation
from typing import List
import heapq

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = -2
        while abs(i) != len(nums) + 1 and int(nums[i]) >= int(nums[i + 1]):
            i -= 1
        if abs(i) == len(nums) + 1:
            nums.sort()
            return
        a = int(nums[i])
        idx = i + 1
        for j in range(i + 2, 0):
            if int(nums[j]) <= a:
                idx = j - 1
                break
            else:
                idx = j
        nums[i], nums[idx] = nums[idx], nums[i]
        for j in range(-1, i // 2, -1):
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        return


if __name__ == '__main__':
    a = ["1", "5", "1"]
    s = Solution()
    s.nextPermutation(a)
    print(a)