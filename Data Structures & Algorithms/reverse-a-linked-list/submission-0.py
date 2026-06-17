# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if empty return head
        if not head:
            return head
        cur = head
        prev = None

        # loop through, and implement reverse logic
        while cur.next != None:
            
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        cur.next = prev
        return cur