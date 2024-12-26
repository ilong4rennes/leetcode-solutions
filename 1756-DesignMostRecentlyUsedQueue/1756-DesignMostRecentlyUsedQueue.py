class MRUQueue:

    def __init__(self, n: int):
        self.capacity = n
        self.queue = []
        start = 1
        for i in range(n):
            self.queue.append(start)
            start += 1

    def fetch(self, k: int) -> int:
        element = self.queue[k - 1]
        self.queue.pop(k - 1)
        self.queue.append(element)
        return element

        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)