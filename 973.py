# K Closest Points to Origin
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        h = []
        i = 0
        for x, y in points:
            heapq.heappush(h, (x ** 2 + y ** 2, i))
            i += 1
        return [points[heapq.heappop(h)[1]] for _ in range(K)]

if __name__ == '__main__':
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    s = Solution()
    print(s.kClosest(points, K))