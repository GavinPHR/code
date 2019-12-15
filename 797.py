# All Paths From Source to Target
from collections import deque
from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        d = dict()
        d[target] = [[target]]
        def fillN(n):
            d[n] = []
            for i in graph[n]:
                if i not in d:
                    fillN(i)
                for ns in d[i]:
                    d[n].append([n]+ns)
        fillN(0)
        return d[0]




s = Solution()
print(s.allPathsSourceTarget([[1,2], [3], [3], []]))