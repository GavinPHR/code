#  Implement Rand10() Using Rand7()
import random

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand7(self):
        return random.randint(1,7)

    def rand10(self):
        prod = 7 * (self.rand7() - 1) + self.rand7()
        while prod > 40:
            prod = 7 * (self.rand7() - 1) + self.rand7()
        return 10 if prod % 10 == 0 else prod % 10

if __name__ == '__main__':
    acc = 0
    s = Solution()
    for _ in range(100000):
        acc += s.rand10()
    print(acc / 100000)