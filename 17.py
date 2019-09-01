# Letter Combinations of a Phone Number
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        d = {'2': ['a','b','c'],
             '3': ['d','e','f'],
             '4': ['g','h','i'],
             '5': ['j','k','l'],
             '6': ['m','n','o'],
             '7': ['p','q','r','s'],
             '8': ['t','u','v'],
             '9': ['w','x','y','z'],}
        s1 = ['']
        s2 = []
        def put(f: List[List[str]], t: List[List[str]], l: List[str]):
            while f:
                tmp = f.pop()
                for c in l:
                    tmp2 = list(tmp)
                    tmp2.append(c)
                    t.append(tmp2)
            return
        for digit in digits:
            if s1: put(s1, s2, d[digit])
            else: put(s2, s1, d[digit])
        if s1:
            s1 = ["".join(x) for x in s1]
            return s1
        else:
            s2 = ["".join(x) for x in s2]
            return s2



s = Solution()
print(s.letterCombinations("2"))