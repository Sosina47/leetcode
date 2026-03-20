# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p = self.traverse(p)
        q = self.traverse(q)

        return p == q

    def traverse(self, node):
        if not node:
            return []
        
        output = []
        stack = [node]

        while stack:
            tree = stack.pop()

            if type(tree) == int or not tree:
                output.append(tree)

            else:
                stack.append(tree.val) 

                stack.append(tree.right)

                stack.append(tree.left)

        return output
                
