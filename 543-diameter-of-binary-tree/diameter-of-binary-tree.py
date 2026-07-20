# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def check_height(node):
            if not node:
                return 0
            
            left_height = check_height(node.left)
            right_height = check_height(node.right)
            
            self.diameter = max(self.diameter, left_height + right_height)
            
            return 1 + max(left_height, right_height)
        
        check_height(root)
        return self.diameter