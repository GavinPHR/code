# Reveal Cards In Increasing Order
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if not deck: return []
        ans = [None] * (2 * len(deck) - 1)
        deck.sort(reverse=True)
        ans[-1] = deck[0]
        front = -2
        back = -1
        for n in deck[1:]:
            ans[front] = ans[back]
            ans[front - 1] = n
            back -= 1
            front -= 2
        return ans[:len(deck)]


s = Solution()
print(s.deckRevealedIncreasing([17,13,11,2,3,5,7]))