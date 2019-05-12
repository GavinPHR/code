# Design HashSet

class MyHashSet:

    def __init__(self):
        self.SET = [[] for i in range(113)]

    def add(self, key: int) -> None:
        s = self.SET[key%113]
        for k in s:
            if k == key:
                return
        s.append(key)
    def remove(self, key: int) -> None:
        s = self.SET[key%113]
        for k in s:
            if k == key:
                s.remove(k)
                break
    def contains(self, key: int) -> bool:
        #print(self.SET)
        s = self.SET[key % 113]
        for k in s:
            if k == key:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

if __name__ == '__main__':
    h = MyHashSet()
    h.add(1)
    h.add(2)
    print(h.contains(1))
    #true
    print(h.contains(3))
    #false(not found)
    h.add(2)
    print(h.contains(2))
    #true
    h.remove(2)
    print(h.contains(2))
    #false(already
    #removed)