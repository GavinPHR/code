# Matrix Cells in Distance Order
from typing import List

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        #counting sort
        d = dict()
        count = [0] * (R + C)
        for i in range(R):
            for j in range(C):
                val = abs(r0 - i) + abs(c0 - j)
                if d.get(val): d.get(val).append([i, j])
                else: d[val] = [[i, j]]
                count[val] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        ans = [None] * count[-1]
        for k in d:
            stack = d.get(k)
            while stack:
                t = stack.pop()
                ans[count[k] - 1] = t
                count[k] -= 1
        return ans

        #Sorting O(nlogn) sol
        # l = [[x, y] for x in range(R) for y in range(C)]
        # l.sort(key=lambda x: abs(r0 - x[0]) + abs(c0 - x[1]))
        # return l

s = Solution()
print(s.allCellsDistOrder(2,3,1,2))