from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = deque([(root, 0)])
        
        while queue:
            level_size = len(queue)
            first_idx = queue[0][1]
            last_idx = queue[-1][1]
            
            max_width = max(max_width, last_idx - first_idx + 1)
            
            for _ in range(level_size):
                node, idx = queue.popleft()
                curr_idx = idx - first_idx
                
                if node.left:
                    queue.append((node.left, 2 * curr_idx))
                if node.right:
                    queue.append((node.right, 2 * curr_idx + 1))
                    
        return max_width