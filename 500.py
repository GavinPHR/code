# Keyboard Row
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        d = {"q":1,"w":1,"e":1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1,
             'a':2,'s':2,'d':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,
             'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3}
        ans = []
        for w in words:
            tmp = w.lower()
            n = d[tmp[0]]
            flag = True
            for c in tmp:
                if d[c] != n:
                    flag = False
            if flag: ans.append(w)
        return ans

s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
