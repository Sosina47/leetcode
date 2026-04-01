# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] += 1
        count = 0

        def countSum(root, cur):
            nonlocal count
            nonlocal prefix
            
            if not root:
                return 

            cur += root.val
            count += prefix[cur - targetSum]
            prefix[cur] += 1
            
            countSum(root.left, cur)
            countSum(root.right, cur)

            prefix[cur] -= 1

        countSum(root, 0)
        return count