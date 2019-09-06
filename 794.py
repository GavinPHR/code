# Valid Tic-Tac-Toe State
from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        turns = 0
        rows = [0, 0, 0]
        cols = [0, 0, 0]
        diag = 0
        antid = 0
        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n == "X":
                    turns += 1
                    rows[i] += 1
                    cols[j] += 1
                    if i == j: diag += 1
                    if i + j == 2: antid += 1
                if n == "O":
                    turns -= 1
                    rows[i] -= 1
                    cols[j] -= 1
                    if i == j: diag -= 1
                    if i + j == 2: antid -= 1
        xwin = any(x == 3 for x in rows) or any(x == 3 for x in cols) or diag == 3 or antid == 3
        ywin = any(x == -3 for x in rows) or any(x == -3 for x in cols) or diag == -3 or antid == -3
        if (xwin and turns == 0) or (ywin and turns == 1): return False
        return (turns == 0 or turns == 1) and (not xwin or not ywin)
