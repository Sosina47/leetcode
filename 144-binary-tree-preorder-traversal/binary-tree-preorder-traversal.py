# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root):
        if root == None:
            return []

        output = []
        output.append(root.val)

        output.extend(self.traverse(root.left))
        output.extend(self.traverse(root.right))

        return output

        
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        output = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        
        return output
        
        
        
        
        # return self.traverse(root)