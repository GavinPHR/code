# Find and Replace Pattern
from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        l = len(words[0])
        ans = []
        for w in words:
            d = dict()
            mapped = set()
            flag = True
            for i in range(l):
                t = d.get(pattern[i])
                if t:
                    if t != w[i]:
                        flag = False
                        break
                else:
                    if w[i] in mapped:
                        flag = False
                        break
                    d[pattern[i]] = w[i]
                    mapped.add(w[i])
            if flag: ans.append(w)
        return ans

s = Solution()
print(s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],"abb"))