# Number of Segments in a String

class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        flag = False
        for c in s:
            if c == " ":
                flag = False
            else:
                if flag == True:
                    continue
                else:
                    ans += 1
                    flag = True
        return ans