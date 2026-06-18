# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = self.helper(root, [])
        if not result:
            return []
        return result

    def helper(self, root: Optional[TreeNode], result: List[int]) -> List[int]:
        if not root:
            return
        self.helper(root.left, result)
        result.append(root.val)
        self.helper(root.right, result)

        return result