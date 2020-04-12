class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            l1 = heapq.heappop(stones)
            l2 = heapq.heappop(stones)
            if l1 == l2:
                continue
            else:
                heapq.heappush(stones, l1-l2)
        return -stones[0] if stones else 0
                