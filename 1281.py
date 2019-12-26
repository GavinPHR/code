# Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        xs = [int(x) for x in str(n)]
        product = 1
        for x in xs: product *= x
        return product - sum(xs)