# Maximum Frequency Stack
import collections
import heapq
class FreqStack:

    def __init__(self):
        self.count = collections.Counter()
        self.order = [[],[]]
        self.acc = 0

    def push(self, x: int) -> None:
        self.count[x] += 1
        try:
            heapq.heappush(self.order[self.count[x]], (self.acc, x))
        except Exception:
            self.order.append([])
            heapq.heappush(self.order[self.count[x]], (self.acc, x))
        self.acc -= 1

    def pop(self) -> int:
        print(self.order)
        _, ans = heapq.heappop(self.order[-1])
        self.count[ans] -= 1
        if not self.order[-1]:
            self.order.pop()
        return ans



# Your FreqStack object will be instantiated and called as such:

if __name__ == '__main__':
    obj = FreqStack()
    obj.push(5)
    obj.push(7)
    obj.push(5)
    obj.push(7)
    obj.push(4)
    obj.push(5)
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())