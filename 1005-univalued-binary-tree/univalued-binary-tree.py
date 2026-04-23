# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True

        queue = deque()
        queue.append(root) 

        while queue: 
            node = queue.popleft()

            if node.right and node.right.val != node.val:
                return False

            if node.left and node.left.val != node.val:
                return False

            if node.right: 
                queue.append(node.right)

            if node.left: 
                queue.append(node.left)

        return True