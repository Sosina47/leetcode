# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, False, False, 0)

    def traverse(self, root, parent, gp, total):
        if not root:
            return total
        cur = total + root.val if gp else 0
        
        gp, parent = parent, root.val % 2 == 0

        left = self.traverse(root.left, parent, gp, total) 
        right = self.traverse(root.right, parent, gp, total) 

        return left + right + cur