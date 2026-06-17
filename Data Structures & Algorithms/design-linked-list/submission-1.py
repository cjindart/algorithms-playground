class ListNode:

    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur != self.tail and i < index:
            i += 1
            cur = cur.next
        if i == index and cur != self.tail:
            return cur.val
        return -1


    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        newNode.prev = self.head

        self.head.next.prev = newNode
        self.head.next = newNode
        
        
    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head.next
        i = 0
        while cur != self.tail and i < index:
            i += 1
            cur = cur.next
        if i == index:

            newNode = ListNode(val)
            newNode.prev = cur.prev
            newNode.next = cur

            cur.prev.next = newNode
            cur.prev = newNode

        # if jump out, dont add (out of bounds)
        return

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        i = 0
        while cur != self.tail and i < index:
            i += 1
            cur = cur.next
        if i == index and cur != self.tail:
            # delete the node
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
        # jump out, return nothing deleted (OOB)
        return

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)