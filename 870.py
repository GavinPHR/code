# Advantage Shuffle
from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        marked = [False] * len(A)
        C = sorted((x for x in range(len(A))), key=lambda i: -B[i])
        A.sort(reverse=True)
        i = 0
        j = 0
        for n in A:
            while i < len(B) and n <= B[C[i]]:
                i += 1
            if i == len(B):
                break
            B[C[i]] = n
            marked[C[i]] = True
            j += 1
        g = iter(A[j:])
        for i, b in enumerate(marked):
            if not b:
                B[i] = next(g)
        return B





s = Solution()
print(s.advantageCount([12,24,8,32],[13,25,32,11]))