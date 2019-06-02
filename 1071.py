# Greatest Common Divisor of Strings

class Solution:
    def split(self, s):
        n = len(s)
        ans = set()
        for i in range(2, n // 2 + 1):
            if n % i != 0:
                continue
            seg = n // i
            flag = True
            for j in range(0, i - 1):
                if s[j * seg:(j + 1) * seg] != s[(j + 1) * seg:(j + 2) * seg]:
                    flag = False
                    break
            if flag:
                ans.add(s[0:seg])
        return ans

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def split(s):
            n = len(s)
            ans = set()
            for i in range(1, n // 2 + 1):
                if n % i != 0:
                    continue
                seg = n // i
                flag = True
                for j in range(0, i - 1):
                    if s[j * seg:(j + 1) * seg] != s[(j + 1) * seg:(j + 2) * seg]:
                        flag = False
                        break
                if flag:
                    ans.add(s[0:seg])
            return ans
        one, two = split(str1), split(str2)
        ans = list(one & two)
        if not ans:
            return ""
        ans.sort(key=lambda x:-len(x))
        return ans[0]

if __name__ == '__main__':
    str1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    str2 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    s = Solution()
    print(s.gcdOfStrings(str1, str2))