# Bag of Tokens
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        print(tokens)
        max = 0
        cur = 0
        l, r= 0, len(tokens) - 1
        if P - tokens[0] < 0:
            return 0
        while l <= r:
            while P - tokens[l] >= 0:
                P -= tokens[l]
                print(tokens[l])
                cur += 1
                if cur > max:
                    max = cur
                if l == r:
                    break
                l += 1
            if l >= r:
                break
            if cur != 0:
                P += tokens[r]
                if r > l:
                    cur -= 1
                    r -= 1
        return max


if __name__ == '__main__':
    s = Solution()
    print(s.bagOfTokensScore([91,4,75,70,66,71,91,64,37,54], 20))