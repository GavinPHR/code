# Max Consecutive Ones III
from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, right = 0, 0
        count0 = 0
        ans = 0
        while right < len(A):
            while right < len(A) and count0 <= K:
                count0 += 1 if A[right] == 0 else 0
                right += 1
                if count0 > K: break
                print(left, right, count0)
                ans = max(ans, right - left)
            while count0 > K:
                count0 -= 1 if A[left] == 0 else 0
                left += 1
        return ans





A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
s = Solution()
print(s.longestOnes(A,K))



