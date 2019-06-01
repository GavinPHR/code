# Satisfiability of Equality Equations
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        eq = set()
        neq = set()
        for e in equations:
            if e[1] == "!":
                if e[0] == e[3]:
                    return False
                neq.add((e[0],e[3]))
                neq.add((e[3],e[0]))
            else:
                eq.add((e[0],e[3]))
        flag = True
        while flag:
            print(eq)
            closure = set()
            for fst, snd in eq:
                if (snd, fst) not in eq:
                    closure.add((snd, fst))
                for l, r in eq:
                    if snd == l:
                        closure.add((fst, r))
            if closure.issubset(eq):
                flag = False
            else:
                eq.update(closure)
        return False if eq & neq else True




if __name__ == '__main__':
    s = Solution()
    a = ["a==b","e==c","b==c","a!=e"]
    print(s.equationsPossible(a))