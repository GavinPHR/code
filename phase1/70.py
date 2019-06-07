# Climbing Stairs


class Solution:
    def climbStairs(self, n: int) -> int:
        p = 1
        cur = 1
        for i in range(1, n):
            p, cur = cur, p + cur
        return cur

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))