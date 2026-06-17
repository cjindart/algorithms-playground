# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # traverse each list, add smaller to new list, if same, add both

        # if both empty, return 
        if not list1 and not list2:
            return list1
        # if list 1 empty, return list 2
        elif not list1:
            return list2
        # vice versa
        elif not list2:
            return list1
        
        dummy = ListNode()
        tail = dummy

        cur1 = list1
        cur2 = list2

        # main loop, rearrange nodes in order
        while cur1 and cur2:
            if cur1.val < cur2.val:
                tail.next = cur1
                tail = cur1
                cur1 = cur1.next
            else:
                tail.next = cur2
                tail = cur2
                cur2 = cur2.next
        
        # jump out, one list empty
        if cur1:
            tail.next = cur1
        if cur2:
            tail.next = cur2
        return dummy.next




