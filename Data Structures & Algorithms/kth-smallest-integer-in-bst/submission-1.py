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
        self.inOrder(root, k)
        return self.val


    def inOrder(self, root: Optional[TreeNode], k: int):

        if not root:
            return
        self.inOrder(root.left, k)
        self.i += 1
        if self.i == k:
            self.val = root.val
        else:
            self.inOrder(root.right, k)

        

