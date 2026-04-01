# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None

        head_index = inorder.index(preorder[0])

        left = self.buildTree(preorder[1: head_index + 1], inorder[:head_index])
        right = self.buildTree(preorder[head_index + 1 :], inorder[head_index + 1:])

        return TreeNode(preorder[0], left, right)

        
        


