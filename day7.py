class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        return sum(1 if a+1 in s else 0 for a in arr)