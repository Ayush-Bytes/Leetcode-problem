# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        l_t_r = True

        while queue:
            l_size = len(queue)
            curr_l = deque()

            for _ in range(l_size):
                node = queue.popleft()

                if l_t_r:
                    curr_l.append(node.val)
                else:
                    curr_l.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(curr_l))
            l_t_r = not l_t_r
        
        return res