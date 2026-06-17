class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        size = len(self.queue)

        for i in range(size - 1):
            item = self.queue.pop(0)
            self.queue.append(item)
        item = self.queue.pop(0)
        return item


    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if not self.queue:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()