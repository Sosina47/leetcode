# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        operations = self.minMoves(root)
        return operations[1]
        
    def minMoves(self, root):
        if not root:
            return [0, 0]

        left = self.minMoves(root.left)
        right = self.minMoves(root.right)

        coins = left[0] + right[0]
        moves = left[1] + right[1]

        coins += root.val - 1
        moves += abs(coins)

        return [coins, moves]