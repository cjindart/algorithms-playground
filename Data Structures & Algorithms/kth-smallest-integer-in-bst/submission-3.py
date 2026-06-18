# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    i = 0
    val = None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        self.inOrder(root, k)
        return self.val


    def inOrder(self, root: Optional[TreeNode], k: int):
        if not root or self.val is not None:
            return
        self.inOrder(root.left, k)
        if self.val is None:
            self.i += 1
            if self.i == k:
                self.val = root.val
                return
                
        self.inOrder(root.right, k)

        

