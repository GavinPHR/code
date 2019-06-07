# To Lower case

class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()


if __name__ == '__main__':
    str = "HellP"
    s = Solution()
    print(s.toLowerCase(str))
