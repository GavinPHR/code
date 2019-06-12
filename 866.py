# Prime Palindrome

class Solution:
    def primePalindrome(self, N: int) -> int:
        def isPrime(n):
            if n < 2: return False
            for i in range(2, int(n ** (0.5) + 1)):
                if n % i == 0:
                    return False
            return True

        if 11 >= N and N > 7:
            return 11

        for i in range(10 ** 6):
            palindromicroot = str(i)
            rightpart = palindromicroot[-2::-1]
            num = int(palindromicroot + rightpart)
            print(num)
            if num >= N and isPrime(num):
                return num

s = Solution()
print(s.primePalindrome(8))