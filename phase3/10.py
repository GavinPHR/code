# Regular Expression Matching
from collections import defaultdict
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        fsm = FSM(p)
        fsm.transitionString(s)
        return fsm.accept()

class FSM:
    Sigma = [chr(97+i) for i in range(26)]
    delta = dict()
    currentState = {0}
    eDelta = dict()

    def __init__(self, regex: str):
        i = 0
        regex = list(regex[::-1])
        while regex:
            self.delta[i] = defaultdict(list)
            current = regex.pop()
            star = True if (regex and regex[-1] == '*') else False
            if star:
                regex.pop()
                self.eDelta[i] = i + 1
                i += 1
                self.delta[i] = defaultdict(list)
                if current == '.':
                    for c in self.Sigma:
                        self.delta[i][c].append(i)
                else:
                    self.delta[i][current].append(i)
                self.eDelta[i] = i + 1
                i += 1
            else:
                if current == '.':
                    for c in self.Sigma:
                        self.delta[i][c].append(i + 1)
                else:
                    self.delta[i][current].append(i + 1)
                i += 1
        self.acceptState = i
        if not self.delta.get(i):
            self.delta[i] = defaultdict(list)

    def accept(self):
        # print(self.eClose(self.currentState), self.acceptState)
        # print(self.delta)
        if self.acceptState in self.eClose(self.currentState):
            return True
        else:
            return False

    def eClose(self, state: set):
        prev = state.copy()
        closure = state.copy()
        for s in prev:
            if self.eDelta.get(s):
                closure.add(self.eDelta.get(s))
        while closure != prev:
            prev = closure.copy()
            for s in prev:
                if self.eDelta.get(s):
                    closure.add(self.eDelta.get(s))
        return closure

    def transitionString(self, s):
        for c in s:
            self.transitionChar(c)

    def transitionChar(self, c):
        state = self.eClose(self.currentState)
        nextState = set()
        for s in state:
            nextState.update(self.delta[s].get(c, []))
        self.currentState = nextState


s = Solution()
print(s.isMatch("ab",".*c"))


