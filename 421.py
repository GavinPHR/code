# Maximum XOR of Two Numbers in an Array
from typing import List

class Solution:
    def findMaximumXOR(self, nums):
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            print(bin(answer^1)[2:], list(map(lambda x: bin(x)[2:], prefixes)))
            print(any(answer ^ 1 ^ p in prefixes for p in prefixes))
            answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)
        return answer

    #https: // kingsfish.github.io / 2017 / 12 / 15 / Leetcode - 421 - Maximum - XOR - of - Two - Numbers - in -an - Array /


s = Solution()
print(s.findMaximumXOR([3, 10, 5, 25, 2, 8]))