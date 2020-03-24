# Broken Calculator
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if Y <= X: return X - Y
        count = 0
        while Y > X:
            if Y % 2 == 1:
                Y = (Y + 1) // 2
                count += 2
            else:
                Y //= 2
                count += 1
        return count + (X - Y)