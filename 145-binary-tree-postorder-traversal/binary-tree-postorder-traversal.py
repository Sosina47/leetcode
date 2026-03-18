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
    #     output.extend(self.traverse())

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        output = []

        while stack:
            node = stack.pop()

            if node == None:
                continue
            
            if type(node) == int:
                output.append(node)

            else:
                stack.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return output