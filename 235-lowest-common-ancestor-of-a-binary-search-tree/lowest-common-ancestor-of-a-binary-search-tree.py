# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            # If both values are greater than current node, LCA lies in right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both values are smaller than current node, LCA lies in left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # If one is smaller and one is larger (or one equal to curr), we found the split point (LCA)
            else:
                return curr