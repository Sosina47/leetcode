# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        inf = float("inf")

        def countDepth(root):
            nonlocal inf

            if not root.left and not root.right:
                return 1

            left = countDepth(root.left) if root.left else inf
            right = countDepth(root.right) if root.right else inf

            return 1 + min(left, right)

        if not root:
            return 0
            
        return countDepth(root)