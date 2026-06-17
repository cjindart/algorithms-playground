class MyStack:

    def __init__(self):
        self.array = []
        self.size = 0

    def push(self, x: int) -> None:
        self.array.append(x)
        self.size += 1

    def pop(self) -> int:
        elem = self.array[-1]
        del self.array[-1]
        self.size -= 1
        return elem

    def top(self) -> int:
        return self.array[-1]

    def empty(self) -> bool:
        if self.size == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()