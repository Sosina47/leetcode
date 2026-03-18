# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root):
        output = []
        if root == None:
            return []

        output.append(root.val)
        output.extend(self.traverse(root.left))
        output.extend(self.traverse(root.right))

        return output

        
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traverse(root)