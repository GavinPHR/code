# Pancake Sorting
from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans= []
        for i in range(len(A), 1, -1):
            print(A)
            idx = A.index(i) + 1
            if idx == i: continue
            if idx == 1:
                for j in range(i // 2):
                    A[j], A[i - j - 1] = A[i - j - 1], A[j]
                ans.append(i)
                continue
            for j in range(idx // 2):
                A[j], A[idx - j - 1] = A[idx - j - 1], A[j]
            ans.append(idx)
            for j in range(i // 2):
                A[j], A[i - j - 1] = A[i - j - 1], A[j]
            ans.append(i)
        print(A)
        print(ans)
        return ans

s = Solution()
print(s.pancakeSort([3,2,4,1]))