# Valid Perfect Square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        x = num // 2
        while True:
            if x ** 2 <= num:
                break
            x = (x + num / x) // 2
        return True if int(x) ** 2 == num else False

if __name__ == '__main__':
    s = Solution()
    for i in range(0,101):
        print(i, s.isPerfectSquare(i))