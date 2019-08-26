# Relative Sort Array
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if not arr2:
            arr1.sort()
            return
        d = {x: 0 for x in arr2}
        s = set(arr2)
        notIn = []
        for n in arr1:
            if n in s:
                d[n] = d.get(n) + 1
            else:
                notIn.append(n)
        print(d)
        notIn.sort()
        ans = []
        for x in arr2:
            for _ in range(d.get(x)):
                ans.append(x)
        return ans + notIn

s = Solution()
print(s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))