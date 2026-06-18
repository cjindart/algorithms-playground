# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque()

        if root:
            queue.append(root)
        
        level = 0
        while len(queue) > 0:
            n = len(queue)
            for i in range(n):
                cur = queue.popleft()
                if i == n-1:
                    result.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                
            level += 1

        return result