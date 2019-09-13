# Friend Circles
from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        d = {}
        n = len(M)
        for i in range(n):
            if i not in d:
                d[i] = set([i])
            for j in range(i + 1, n):
                if M[i][j] and j not in d:
                    d[j] = d[i]
                    d[j].add(j)
                elif M[i][j] and j in d:
                    for x in d[i]:
                        d[x] = d[j]
                        d[x].add(x)
        print(d.values())
        return len(set(map(tuple, d.values())))




s = Solution()
print(s.findCircleNum([[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                       [0,1,0,0,0,1,0,0,0,0,0,0,0,0,0],
                       [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                       [1,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
                       [0,1,0,0,0,1,0,0,0,0,0,0,1,0,0],
                       [0,0,0,0,0,0,1,0,0,0,0,1,0,0,0],
                       [0,0,0,0,0,0,0,1,0,0,0,1,1,0,0],
                       [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                       [0,0,0,0,0,0,1,1,0,0,1,1,0,0,1],
                       [0,0,0,0,1,1,0,1,0,0,0,0,1,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                       [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1]]))
