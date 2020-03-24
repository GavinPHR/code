# Check If It Is a Straight Line
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        p1, p2 = coordinates[0], coordinates[1]
        # y = kx + b
        try:
            k = (p1[1] - p2[1]) / (p1[0] - p2[0])
        except ZeroDivisionError:
            for x, _ in coordinates[2:]:
                if x != p1[0]: return False
                return True
        b = p1[1] - k * p1[0]
        for x, y in coordinates[2:]:
            if k * x + b != y: return False
        return True
