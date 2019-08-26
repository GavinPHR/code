# Flood Fill
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        explored = set()
        stack = [(sr, sc)]
        c = image[sr][sc]
        image[sr][sc] = newColor
        def neighbour(x, y):
            for a, b in (x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1):
                if a >=0 and a < n and b >= 0 and b < m:
                    if (a, b) in explored: continue
                    yield (a, b)
        while stack:
            current = stack.pop()
            for a, b in neighbour(*current):
                if image[a][b] == c:
                    image[a][b] = newColor
                    stack.append((a, b))
            explored.add(current)
        return image

s = Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))