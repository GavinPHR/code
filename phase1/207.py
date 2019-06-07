# Course Schedule
from typing import List


class Solution:
    def parseEdges(self, num: int, edges: List[List[int]]):
        dict = {i:[] for i in range(num)}
        for (b, a) in edges:
            dict.get(a).append(b)
        return dict

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfsFrom(i):
            state[i] = 0
            for vertex in graph.get(i):
                if state[vertex] == 1:
                    dfsFrom(vertex)
                elif state[vertex] == 0:
                    raise Exception
            state[i] = -1
        graph = self.parseEdges(numCourses, prerequisites)
        state = [1] * numCourses
        for i in range(numCourses):
            if state[i] == 1:
                try:
                    dfsFrom(i)
                except Exception:
                    return False
        return True