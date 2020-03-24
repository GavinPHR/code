# Surrounded Regions
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if board == [[]] or board == []: return
        a, b = len(board), len(board[0])
        seen = set()
        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n == 'O' and (i, j) not in seen:
                    local = set()
                    stack = [(i, j)]
                    flag = True
                    while stack:
                        x, y = stack.pop()
                        local.add((x, y))
                        for xx, yy in (0, 1), (0, -1), (1, 0), (-1, 0):
                            xxx, yyy = x + xx, y + yy
                            if (xxx, yyy) in local:
                                continue
                            elif xxx >= a or xxx < 0:
                                flag = False
                                continue
                            elif yyy >= b or yyy < 0:
                                flag = False
                                continue
                            elif board[xxx][yyy] == 'O':
                                stack.append((x + xx, y + yy))
                            else:
                                continue
                    seen.update(local)
                    if flag:
                        for x, y in local:
                            board[x][y] = 'X'

s = Solution()
b = [['X', 'X', 'X', 'X'],
     ['X', 'O', 'O', 'X'],
     ['X', 'X', 'O', 'X'],
     ['X', 'O', 'X', 'X']]
s.solve(b)
print(b)

