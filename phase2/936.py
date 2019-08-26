#  Stamping The Sequence
from typing import List
import collections

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(stamp), len(target)
        poss = set()
        poss.add(stamp)
        l = list(stamp)
        for i in range(n - 1):
            l[i] = "?"
            poss.add("".join(l))
        tmpset = set()
        for s in poss:
            l = list(s)
            for i in range(n - 1, 0, -1):
                if l[i - 1] == "?": break
                l[i] = "?"
                tmpset.add("".join(l))
        print(tmpset)
        poss.update(tmpset)
        print(poss)
        depth = 0
        l = list(target)
        ans = []
        while depth <= 10:
            flag = True
            for i, c in enumerate(l):
                if "".join(l[i:i + n]) in poss:
                    flag = False
                    ans.append(i)
                    for j in range(i, i + n):
                        l[j] = "?"
            print(l)
            if flag: break
            depth += 1
        for c in l:
            if c != "?":
                return []
        ans.reverse()
        return ans






s = Solution()
print(s.movesToStamp("zbs","zbzbsbszbssbzbszbsss"))
