# Max Points on a Line
from typing import List
import collections


class Solution:
    lines = set()
    count = collections.Counter()
    def lineParam(self, p1: List[int], p2: List[int]) -> (int, int, int):
        a = p1[1] - p2[1]
        b = p2[0] - p1[0]
        c = - a * p1[0] - b * p1[1]
        return a, b, c

    def getLines(self, points: List[List[int]]):
        marked = [False for i in range(len(points))]
        for i in range(len(points)):
            for j in range(len(points)):
                if j == i: continue
                if not marked[j]:
                    if points[i] == points[j]:
                        self.lines.add(self.lineParam(points[i], [0,0]))
                    else:
                        self.lines.add(self.lineParam(points[i],points[j]))
            marked[i] = True

    def isOnLine(self, p: List[int], line: (int, int, int)) -> bool:
        if line == (0,0,0) and p != [0,0]:
            return False
        return line[0] * p[0] + line[1] * p[1] + line[2] == 0

    def maxPoints(self, points: List[List[int]]) -> int:
        if points == []: return 0
        if len(points) == 1: return 1
        self.getLines(points)
        for p in points:
            for line in self.lines:
                if self.isOnLine(p, line):
                    self.count[line] += 1
        ans = self.count.most_common(1)[0][1]
        self.lines.clear()
        self.count.clear()
        return ans


if __name__ == '__main__':
    A = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    B = [[1,1],[2,2],[3,3]]
    C = [[0,0],[0,0]]
    D = [[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]]
    E = [[1,1],[1,1],[1,1]]
    s = Solution()
    print(s.maxPoints(D))
