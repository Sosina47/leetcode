# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        head = TreeNode(postorder.pop())

        if postorder:
            r = preorder.index(postorder[-1])

            left = self.constructFromPrePost(preorder[1:r], postorder[:r - 1])
            right = self.constructFromPrePost(preorder[r:], postorder[r - 1:])

        else:
            left = right = None
        
        head.left = left
        head.right = right

        return head