# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        remainder = set()

        def traverse(root):
            if root == None:
                return False

            if root.val in remainder:
                return True
            
            remainder.add(k - root.val)
            
            return traverse(root.left) or traverse(root.right)
        
        return traverse(root)