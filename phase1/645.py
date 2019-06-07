# Set Mismatch
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        marked = [False] * n
        s = 0
        dup = None
        for i in nums:
            if marked[i - 1] == True:
                dup = i
            else:
                marked[i - 1] = True
            s += i
        diff = n * (n + 1) / 2 - s
        print(s)
        print(diff)
        return (dup, dup + diff)

if __name__ == '__main__':
    s = Solution()
    print(s.findErrorNums([1,2,2,4]))