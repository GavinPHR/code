# Most Common Word
from typing import List
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        b = set(x.casefold() for x in banned)
        wl = collections.Counter()
        w = []
        for c in paragraph + " ":
            if c in "!?',;. ":
                tmp = "".join(w).casefold()
                if tmp == "":
                    continue
                if tmp in b:
                    w = []
                else:
                    wl[tmp] += 1
                    w = []
            else:
                w.append(c)
        return wl.most_common(1)[0][0]

if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    s = Solution()
    print(s.mostCommonWord(paragraph, banned))
