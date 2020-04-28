class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.start = None
        self.end = None
    
    def append(self, node):
        if not self.start:
            self.start = node
        else:
            self.end.next = node
            node.prev = self.end
        self.end = node
        
    def remove(self, node):
        if node is self.start and node is self.end:
            self.start = None
            self.end = None
        elif node is self.start:
            node.next.prev = None
            self.start = node.next
        elif node is self.end:
            node.prev.next = None
            self.end = node.prev
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

        
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.d = dict()
        self.s = set()
        self.dll = DoublyLinkedList()
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        if not self.dll.start:
            return -1
        return self.dll.start.value

    def add(self, value: int) -> None:
        if value in self.s:
            if value in self.d:
                self.dll.remove(self.d[value])
                del self.d[value]
        else:
            self.s.add(value)
            node = Node(value)
            self.dll.append(node)
            self.d[value] = node


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)