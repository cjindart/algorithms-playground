# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# [0, n-1, 1, n-2, 2, n-3, ...]


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        def rec(root, cur):
            if not cur:
                return root

            root = rec(root, cur.next)
            if not root:
                return None
            tmp = None
            if root == cur or root.next == cur:
                cur.next = None
            else:
                tmp = root.next
                root.next, cur.next = cur, tmp
            
            return tmp
        
        head = rec(head, head.next)

