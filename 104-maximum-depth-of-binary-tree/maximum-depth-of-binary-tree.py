# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node):
        if not node:
            return 0

        left = 1 + self.traverse(node.left)
        right = 1 + self.traverse(node.right)

        return max(left, right)
            
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)

