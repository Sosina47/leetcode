# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sums = []
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum

        if root.left:
            self.findLeaf(root.left, root.val, sums)

        if root.right:
            self.findLeaf(root.right, root.val, sums)

        # print(sums)
        if targetSum in sums:
            return True

        return False


    def findLeaf(self, root, cur_sum, sums):
        cur_sum += root.val
        if not root.right and not root.left:
            return sums.append(cur_sum)

        if not root.right:
            return self.findLeaf(root.left, cur_sum, sums)
        
        if not root.left:
            return self.findLeaf(root.right, cur_sum, sums)

        self.findLeaf(root.left, cur_sum, sums)
        self.findLeaf(root.right, cur_sum, sums)
