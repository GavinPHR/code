# Coin Change
from typing import List


class Solution:
    def recur(self, coins, remain, memoization):

        if remain < 0: return -1
        if remain == 0: return 0
        if memoization[remain - 1] != 0: return memoization[remain - 1]

        min = 2147483647
        for coin in coins:
            res = self.recur(coins, remain - coin, memoization)
            if res >= 0 and res < min:
                min = res + 1

        memoization[remain - 1] = -1 if min == 2147483647 else min
        return memoization[remain - 1]


    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.recur(coins, amount, [0] * amount)


if __name__ == '__main__':
    a = [2, 7, 6]
    s = Solution()
    print(s.coinChange([1,2,5],100))