# Robot Return to Origin

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = [0,0,0,0]
        for c in moves:
            if c == "U":
                count[0] += 1
            elif c == "D":
                count[1] += 1
            elif c == "L":
                count[2] += 1
            elif c == "R":
                count[3] += 1
        if count[0] == count[1] and count[2] == count[3]:
            return True
        else:
            return False


if __name__ == '__main__':
    m = "UD"
    s = Solution()
    print(s.judgeCircle(m))