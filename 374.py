# Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

num = 100

def guess(n):
    if n > 100:
        return -1
    if n < 100:
        return 1
    return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while True:
            mid = (l + r) // 2
            stat = guess(mid)
            if stat == 0:
                return mid
            if stat == -1:
                r = mid - 1
            if stat == 1:
                l = mid + 1
        return

if __name__ == '__main__':
    s = Solution()
    print(s.guessNumber(1000))