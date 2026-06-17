class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0


    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False
        

    def append(self, value: int) -> None:
        newNode = ListNode(value)
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev.next = newNode
        self.tail.prev = newNode


        self.size += 1

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value)
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode

        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        val = self.tail.prev.val

        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -= 1

        return val


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        val = self.head.next.val

        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1

        return val



