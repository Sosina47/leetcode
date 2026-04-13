# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxx = 0

        def solve(root):
            if not root:
                return True, 0, float("inf"), float("-inf")

            l_bst, l_total, l_min, l_max = solve(root.left) 
            r_bst, r_total, r_min, r_max = solve(root.right)

            if not l_bst or not r_bst:
                return False, 0, 0, 0           
                
            if l_max < root.val < r_min:
                l_min = root.val if l_min == float("inf") else l_min
                r_max = root.val if r_max == float("-inf") else r_max

                total = r_total + l_total + root.val
                
                self.maxx = max(self.maxx, total)
                
                return True, total, l_min, r_max

            return False, 0, 0, 0

        solve(root)

        return self.maxx