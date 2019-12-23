# Min Stack

class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, x: int) -> None:
        self.stack.append((x, min(x, self.getMin())))
    def pop(self) -> None:
        if self.stack: self.stack.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return None
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return float('inf')

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())   #--> Returns -3.
minStack.pop()
print(minStack.top())      #--> Returns 0.
print(minStack.getMin())   #--> Returns -2.