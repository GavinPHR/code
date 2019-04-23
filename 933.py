# Number of Recent Calls

class RecentCounter:

    def __init__(self):
        self.record = []

    def ping(self, t: int) -> int:
        self.record.append(t)
        while (t-self.record[0] > 3000): del self.record[0]
        return len(self.record)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

if __name__ == '__main__':
    obj = RecentCounter()
    param_1 = obj.ping(t)