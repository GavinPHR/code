# Largest Time for Given Digits
from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        num = [-float('inf')]
        def permute(n, num):
            if n == 1:
                num_ = A[0] * 1000 + A[1] * 100 + A[2] * 10 + A[3]
                if num_ > num[0] and num_ // 100 < 24 and num_ % 100 < 60:
                    num[0] = num_
            else:
                for i in range(n):
                    A[n-1], A[i] = A[i], A[n-1]
                    permute(n-1, num)
                    A[n - 1], A[i] = A[i], A[n - 1]
        permute(len(A), num)
        return "{0:02}:{1:02}".format(num[0]//100,num[0]%100) if num[0] != -float('inf') else ""

s = Solution()
print(s.largestTimeFromDigits([0,0,0,0]))