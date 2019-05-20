# Reverse Words in a String III

class Solution:
    def reverseWords(self, s: str) -> str:
        def rev(x):
            l = list(x)
            l.reverse()
            return "".join(l)
        return " ".join(rev(x) for x in s.split(" "))


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("a b "))