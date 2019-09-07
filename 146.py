# LRU Cache
from typing import List


class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.current = 0
        self.n = {}
        self.m = 0

    def get(self, key: int) -> int:
        if key in self.d:
            self.n[key] = self.m
            self.m += 1
            return self.d[key]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = value
            self.n[key] = self.m
            self.m += 1
        elif self.current == self.capacity:
            k = min(self.d, key=self.n.get)
            del self.d[k]
            self.d[key] = value
            self.n[key] = self.m
            self.m += 1
        else:
            self.d[key] = value
            self.current += 1
            self.n[key] = self.m
            self.m += 1
        return

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       # returns 1
cache.put(3, 3)    # evicts key 2
print(cache.get(2) )      # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
print(cache.get(1) )    # returns -1 (not found)
print(cache.get(3)  )     # returns 3
print(cache.get(4) )      # returns 4




