# Sliding Puzzle
from typing import List


class Solution:
    ALL = dict()

    def recurBF(self, state, pos0, iter):
        if state not in self.ALL.keys():
            self.ALL[state] = iter
        else:
            if iter < self.ALL.get(state):
                self.ALL[state] = iter
            else:
                return
        if pos0 == 0:
            state1 = (state[1], 0,        state[2], state[3], state[4], state[5])
            self.recurBF(state1, 1, iter + 1)
            state2 = (state[3], state[1], state[2], 0,        state[4], state[5])
            self.recurBF(state2, 3, iter + 1)
        elif pos0 == 1:
            state1 = (0,        state[0], state[2], state[3], state[4], state[5])
            self.recurBF(state1, 0, iter + 1)
            state2 = (state[0], state[2], 0,        state[3], state[4], state[5])
            self.recurBF(state2, 2, iter + 1)
            state3 = (state[0], state[4], state[2], state[3], 0,        state[5])
            self.recurBF(state3, 4, iter + 1)
        elif pos0 == 2:
            state1 = (state[0], 0,        state[1], state[3], state[4], state[5])
            self.recurBF(state1, 1, iter + 1)
            state2 = (state[0], state[1], state[5], state[3], state[4], 0       )
            self.recurBF(state2, 5, iter + 1)
        elif pos0 == 3:
            state1 = (0,        state[1], state[2], state[0], state[4], state[5])
            self.recurBF(state1, 0, iter + 1)
            state2 = (state[0], state[1], state[2], state[4], 0,        state[5])
            self.recurBF(state2, 4, iter + 1)
        elif pos0 == 4:
            state1 = (state[0], 0,        state[2], state[3], state[1], state[5])
            self.recurBF(state1, 1, iter + 1)
            state2 = (state[0], state[1], state[2], 0,        state[3], state[5])
            self.recurBF(state2, 3, iter + 1)
            state3 = (state[0], state[1], state[2], state[3], state[5], 0       )
            self.recurBF(state3, 5, iter + 1)
        else:
            state1 = (state[0], state[1], 0,        state[3], state[4], state[2])
            self.recurBF(state1, 2, iter + 1)
            state2 = (state[0], state[1], state[2], state[3], 0,        state[4])
            self.recurBF(state2, 4, iter + 1)

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        if not self.ALL:
            self.recurBF((1,2,3,4,5,0), 5, 0)
        flattened = tuple((board[i][j] for i in (0, 1) for j in (0, 1, 2)))
        ans = self.ALL.get(flattened)
        if ans == 0: return 0
        return ans if ans else -1

if __name__ == '__main__':
    board = [[1,2,3],[4,5,0]]
    s = Solution()
    print(s.slidingPuzzle(board))
    print(Solution.ALL)