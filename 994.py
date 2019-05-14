# Rotting Oranges
from typing import List
import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        marked = collections.deque()
        flag = True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    flag = False
                if grid[i][j] == 2:
                    marked.append((i, j))
        if flag: return 0
        l = len(marked)
        iter = 0
        while marked:
            print(grid)
            flag = False
            for _ in range(l):
                tmp = marked.popleft()
                i, j = tmp[0], tmp[1]
                if i - 1 > -1:
                    if grid[i - 1][j] == 1:
                        grid[i - 1][j] = 2
                        marked.append((i - 1, j))
                        flag = True
                if i + 1 < len(grid):
                    if grid[i + 1][j] == 1:
                        grid[i + 1][j] = 2
                        marked.append((i + 1, j))
                        flag = True
                if j - 1 > -1:
                    if grid[i][j - 1] == 1:
                        grid[i][j - 1] = 2
                        marked.append((i, j - 1))
                        flag = True
                if j + 1 < len(grid[0]):
                    if grid[i][j + 1] == 1:
                        grid[i][j + 1] = 2
                        marked.append((i, j + 1))
                        flag = True
            l = len(marked)
            if flag:
                iter += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return iter

if __name__ == '__main__':
    a = [[2,1,1],[1,1,0],[0,1,1]]
    b = [[2,1,1],[0,1,1],[1,0,1]]
    c = [[1,2]]
    s = Solution()
    print(s.orangesRotting(c))
    print(c)