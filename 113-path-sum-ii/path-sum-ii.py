# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    output = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.output = []
        self.dfs(root, [], 0, targetSum)
        return self.output

    def dfs(self, root, nums, total, target):
        if not root:
            return 

        total += root.val
        nums.append(root.val)

        if not root.left and not root.right and total == target:
            self.output.append(nums)
            return 
            
        self.dfs(root.left, nums.copy(), total, target)
        self.dfs(root.right, nums.copy(), total, target)


