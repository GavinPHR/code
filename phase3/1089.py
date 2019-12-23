# Duplicate Zeros
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = arr.count(0)
        l = len(arr)
        j = l - 1
        while j + n > l - 1:
            if arr[j] == 0: n -= 1
            j -= 1
        i = j + n
        if i != l - 1:
            for k in range(i + 1, l):
                arr[k] = 0
        while i != -1:
            if arr[j] == 0:
                arr[i] = 0
                arr[i - 1] = 0
                i -= 2
            else:
                arr[i] = arr[j]
                i -= 1
            j -= 1
        print(arr)
        return




s = Solution()
print(s.duplicateZeros([0,0,0,0,0,0,0]))
