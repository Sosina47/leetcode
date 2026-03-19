# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNode(self, node, val):
        if node == None:
            return node

        if node.val > val:
            if node.left:
                return self.findNode(node.left, val)
            else:
                return node

        elif node.val < val:
            if node.right:
                return self.findNode(node.right, val)
            else:
                return node
        
        
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = root
        node = self.findNode(root, val)
        new = TreeNode(val)
        if not node:
            return new
        else:
            if val > node.val:
                node.right = new
            else:
                node.left = new

        return temp
