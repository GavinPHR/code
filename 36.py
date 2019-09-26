# Valid Sudoku
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blks = [set() for _ in range(9)]
        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n == ".": continue
                if n in rows[i]: return False
                rows[i].add(n)
                if n in cols[j]: return False
                cols[j].add(n)
                idx = (i // 3) * 3 + (j // 3)
                if n in blks[idx]: return False
                blks[idx].add(n)
        return True

s = Solution()
b = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(s.isValidSudoku(b))