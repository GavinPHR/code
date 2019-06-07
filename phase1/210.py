# Course Schedule II
from typing import List
from collections import deque

class Solution:
    def parseEdges(self, num: int, edges: List[List[int]]):
        dict = {i:[] for i in range(num)}
        for (b, a) in edges:
            dict.get(a).append(b)
        return dict

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfsFrom(i):
            state[i] = 0
            for vertex in graph.get(i):
                if state[vertex] == 1:
                    dfsFrom(vertex)
                elif state[vertex] == 0:
                    raise Exception
            state[i] = -1
            q.appendleft(i)
        graph = self.parseEdges(numCourses, prerequisites)
        state = [1] * numCourses
        q = deque()
        for i in range(numCourses):
            if state[i] == 1:
                try:
                    dfsFrom(i)
                except Exception:
                    return []
        return list(q)

if __name__ == '__main__':
    s = Solution()
    print(s.parseEdges(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))