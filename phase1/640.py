# Solve the Equation

class Solution:
    def solveEquation(self, equation: str) -> str:
        print(len(equation))
        positive = True
        subtract = False
        xs = 0
        c = 0
        i = 0
        xor = lambda a, b: (a and not b) or (not a and b)
        while i < len(equation):
            if equation[i] == "=":
                positive = True
                subtract = True
                i += 1
                continue
            if equation[i] == "+":
                positive = True
                i += 1
                continue
            elif equation[i] == "-":
                positive = False
                i += 1
                continue
            j = i + 1
            try:
                while j != len(equation) + 1:
                    int(equation[i:j])
                    j += 1
            except:
                pass
            if j < len(equation) + 1 and equation[j - 1] == "x":
                if xor(positive, subtract):
                    xs += int(equation[i:j-1]) if equation[i:j-1] else 1
                else:
                    xs -= int(equation[i:j-1]) if equation[i:j-1] else 1
                i = j
                continue
            else:
                if xor(positive, subtract):
                    c += int(equation[i:j-1])
                else:
                    c -= int(equation[i:j-1])
                i = j - 1
                continue
        if xs == 0 and c == 0:
            return "Infinite solutions"
        if xs != 0 and c == 0:
            return "x=0"
        if xs == 0 and c != 0:
            return "No solution"
        return "x={:.0f}".format(-c / xs)



if __name__ == '__main__':
    e = "x+5-3+x=6+x-2"
    s = Solution()
    print(s.solveEquation("2x+3x-6x=x+2"))