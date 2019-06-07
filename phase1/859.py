# Buddy Strings
import collections

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        pairs = []
        same = collections.Counter()
        for a, b in zip(A,B):
            if len(pairs) > 2:
                return False
            if a == b:
                same[a] += 1
            if same.most_common()[0] > 1:
                return True
            if a != b:
                pairs.append([a,b])
        if len(pairs) != 2:
            return False
        if pairs[0][0] != pairs[1][1] and pairs[0][1] != pairs[1][0]:
            return False
        return True

