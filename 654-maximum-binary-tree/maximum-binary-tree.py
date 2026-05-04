# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        def dfs(i, j):
            if j < i: 
                return None

            maxx = nums.index(max(nums[i:j + 1]))
            root = TreeNode(nums[maxx])
            left = dfs(i, maxx - 1)
            right = dfs(maxx + 1, j)

            root.left = left
            root.right = right

            return root

        return dfs(0, n - 1)