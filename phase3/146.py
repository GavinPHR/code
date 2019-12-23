# LRU Cache
from typing import List

class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

    def pop(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self

    def insert(self, n):
        tmp = self.next
        self.next = n
        n.prev = self
        n.next = tmp
        tmp.prev = n
        return

class LRUCache:

    def __init__(self, capacity: int):
        self.table = {}
        self.capacity = capacity
        self.cacheH = Node(None, None)
        self.cacheT = Node(None, None)
        self.cacheH.next = self.cacheT
        self.cacheT.prev = self.cacheH

    def get(self, key: int) -> int:
        if key not in self.table: return -1
        self.cacheH.insert(self.table[key].pop())
        return self.cacheH.next.val

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            n = self.table[key]
            n.val = value
            self.cacheH.insert(n.pop())
        elif len(self.table) < self.capacity:
            n = Node(key, value)
            self.cacheH.insert(n)
            self.table[key] = n
        else:
            n = self.cacheT.prev.pop()
            del self.table[n.key]
            n = Node(key, value)
            self.cacheH.insert(n)
            self.table[key] = n
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




