class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.miniS = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.size += 1
        if self.miniS:
            if val <= self.miniS[-1]:
                self.miniS.append(val)
        else:
            self.miniS.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.size -= 1
        if val == self.miniS[-1]:
            self.miniS.pop()

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        return self.miniS[-1]