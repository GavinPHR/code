# Game of Life
from typing import List


class Solution:
    #State:
    #0 dead
    #1 alive
    #2 alive -> dead
    #3 dead -> alive
    def gameOfLife(self, board: List[List[int]]) -> None:
        N, M = len(board), len(board[0])
        def neighbouts(i, j):
            for a, b in (i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1):
                if a >= 0 and a < N and b >= 0 and b < M:
                    yield board[a][b]
        for i, row in enumerate(board):
            for j, n in enumerate(row):
                alivecont = 0
                for state in neighbouts(i, j):
                    if state == 1 or state == 2:
                        alivecont += 1
                if n == 1:
                    if alivecont != 2 and alivecont != 3:
                        board[i][j] = 2
                elif n == 0:
                    if alivecont == 3:
                        board[i][j] = 3
                print(i,j,alivecont)
                for row in board:
                    print(row)
                print()
        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n == 2:
                    board[i][j] = 0
                elif n == 3:
                    board[i][j] = 1
        return



if __name__ == '__main__':
    a = [
          [0,1,0],
          [0,0,1],
          [1,1,1],
          [0,0,0]
        ]
    s = Solution()
    s.gameOfLife(a)
    print(a)