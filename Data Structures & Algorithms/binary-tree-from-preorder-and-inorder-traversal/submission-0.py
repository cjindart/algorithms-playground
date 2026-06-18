# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        # get root node
        root_val = preorder[0]
        root = TreeNode(preorder[0])
        
        # find root in inorder, split into right and left
        k = inorder.index(root_val)
        root.right = self.buildTree(preorder[k+1:], inorder[k+1:])
        root.left = self.buildTree(preorder[1:k+1], inorder[:k])
        

        return root