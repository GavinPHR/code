# Count Primes

class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        isPrime = [True for i in range(n)]
        for i in range(2, n):
            if isPrime[i]:
                count += 1
                tmp = i + i
                while tmp < n:
                    isPrime[tmp] = False
                    tmp += i
            else:
                continue
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(2))