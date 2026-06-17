# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # base case
        if not head or not head.next:
            return head
        
        cur = head
        next = cur.next

        new_head = self.reverseList(next)
        ret = new_head

        while new_head:
            if new_head.next:
                new_head = new_head.next
            else:
                break
        new_head.next = cur
        cur.next = None
        
        return ret