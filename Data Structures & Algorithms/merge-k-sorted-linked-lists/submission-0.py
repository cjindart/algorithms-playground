# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        cur = lists[0]
        merged = cur
        for i in range(1, len(lists)):
            # merge each adjacent list, then move to next
            next_list = lists[i]
            merged = self.merge(cur, next_list)
            cur = merged
        
        return merged

            
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1
        ret = None
        cur = None
        if l1.val <= l2.val:
            ret = l1
            cur = l1
            l1 = l1.next
        else:
            ret = l2
            cur = l2
            l2 = l2.next
        
        # merging
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                cur = l1
                l1 = l1.next
            else:
                cur.next = l2
                cur = l2
                l2 = l2.next
        if not l1:
            cur.next = l2
        else:
            cur.next = l1
        return ret




