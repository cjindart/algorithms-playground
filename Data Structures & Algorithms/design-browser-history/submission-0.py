class ListNode:

    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        newNode = ListNode(homepage)
        self.head = newNode
        self.tail = newNode
        self.current = newNode

    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.current.next = newNode
        newNode.prev = self.current
        self.current = newNode
        self.tail = newNode


    def back(self, steps: int) -> str:
        cur = self.current
        i = 0
        while cur != self.head and i < steps:
            i += 1
            cur = cur.prev
        self.current = cur
        return cur.val
        

    def forward(self, steps: int) -> str:
        cur = self.current
        i = 0
        while cur != self.tail and i < steps:
            i += 1
            cur = cur.next
        self.current = cur
        return cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)