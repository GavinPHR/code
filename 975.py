# Odd Even Jump
from typing import List
import bisect

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        E, O = [False] * len(A), [False] * len(A)
        E[-1], O[-1] = True, True
        s = [(A[-1], len(A) - 1)]
        for i in range(len(A) - 2, -1, -1):
            idx = bisect.bisect_left(s, (A[i], i))
            s.insert(idx, (A[i], i))
            if idx == 0:
                if s[idx + 1][0] == s[idx][0]:
                    if E[s[idx + 1][1]]:
                        O[i] = True
                    if O[s[idx + 1][1]]:
                        E[i] = True
                else:
                    if E[s[idx + 1][1]]:
                        O[i] = True
            elif idx == len(s) - 1:
                if idx - 2 > -1 and s[idx - 2][0] == s[idx - 1][0]:
                    newIndex = idx - 1
                    while newIndex > 0 and s[newIndex - 1][0] == s[newIndex][0]:
                        newIndex -= 1
                    if E[s[newIndex][1]]:
                        O[i] = True
                    if O[s[newIndex][1]]:
                        E[i] = True
                else:
                    if O[s[idx - 1][1]]:
                        E[i] = True
            else:
                if idx - 2 > -1 and s[idx - 2][0] == s[idx - 1][0]:
                    newIndex = idx - 1
                    while newIndex > 0 and s[newIndex - 1][0] == s[newIndex][0]:
                        newIndex -= 1
                    if E[s[newIndex][1]]:
                        O[i] = True
                    if O[s[newIndex][1]]:
                        E[i] = True
                elif s[idx + 1][0] == s[idx][0]:
                    if E[s[idx + 1][1]]:
                        O[i] = True
                    if O[s[idx + 1][1]]:
                        E[i] = True
                else:
                    if E[s[idx + 1][1]]:
                        O[i] = True
                    if O[s[idx - 1][1]]:
                        E[i] = True
            print(s)
            print(O)
            print(E)
        return sum(O)




if __name__ == '__main__':
    a = [2,3,1,1,4]
    s = Solution()
    print(s.oddEvenJumps(a))