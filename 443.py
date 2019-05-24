# String Compression
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        p = 0
        acc = 0
        prev = chars[0]
        for c in chars:
            if c == prev:
                acc += 1
            else:
                chars[p] = prev
                p += 1
                if acc > 1:
                    for a in str(acc):
                        chars[p] = a
                        p += 1
                acc = 1
                prev = c
        print(acc)
        chars[p] = prev
        p += 1
        if acc > 1:
            for a in str(acc):
                chars[p] = a
                p += 1
        return p

if __name__ == '__main__':
    a = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    s = Solution()
    print(s.compress(a))
    print(a)