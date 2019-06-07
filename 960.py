# Delete Columns to Make Sorted III
from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        dp = [1] * len(A[0])
        for j in range(len(A[0])):
            for jj in range(0, j):
                inOrder = True
                for i in range(len(A)):
                    if A[i][jj] > A[i][j]:
                        inOrder = False
                        break
                if inOrder:
                    dp[j] = max(dp[j], dp[jj] + 1)
        print(dp)
        return len(A[0]) - max(dp)

s = Solution()
print(s.minDeletionSize(["aabbaa","baabab","aaabab"]))
