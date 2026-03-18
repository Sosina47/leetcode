# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def traverse(self, root):
    #     if not root:
    #         return []

    #     output = []
    #     output.extend(self.traverse(root.left))
    #     output.append(root.val)
    #     output.extend(self.traverse(root.right))

    #     return output
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        output = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node == None:
                continue
                
            if type(node) != int:
                stack.append(node.right)
                stack.append(node.val)
                stack.append(node.left)

            else:
                output.append(node)

        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # return self.traverse(root)