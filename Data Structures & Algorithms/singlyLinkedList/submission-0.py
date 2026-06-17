class ListNode:
    def __init__(self):
        self.val = None
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur != None and i < index:
            cur = cur.next
            i += 1
        if cur and i == index:
            return cur.val
        return -1
        

    def insertHead(self, val: int) -> None:
        new_n = ListNode()
        new_n.val = val
        # no head, also no tail then
        if self.head == None:
            self.head = new_n
            self.tail = new_n
        else:
            # head exists, move it up and add new
            cur_head = self.head
            new_n.next = cur_head
            self.head = new_n

    def insertTail(self, val: int) -> None:
        new_n = ListNode()
        new_n.val = val
        if not self.head:
            self.head = new_n
            self.tail = new_n
        else:
            self.tail.next = new_n
            self.tail = new_n

    def remove(self, index: int) -> bool:
        cur = self.head
        prev = None
        i = 0
        while cur != None and i < index:
            prev = cur
            cur = cur.next
            i += 1
        
        if cur and i == index:
            if prev == None:
                self.head = cur.next
                if not self.head:
                    self.tail = None
            else:
                prev.next = cur.next
                if cur == self.tail:
                    self.tail = prev
            return True
        return False
        
    def getValues(self) -> List[int]:
        result = []
        cur = self.head
        while cur != None:
            result.append(cur.val)
            cur = cur.next
        return result