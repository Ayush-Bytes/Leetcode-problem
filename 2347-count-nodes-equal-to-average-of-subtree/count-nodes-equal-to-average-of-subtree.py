class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def dfs(node):
            nonlocal count
            if not node:
                return 0, 0  # (sum, count)
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1
            
            if curr_sum // curr_count == node.val:
                count += 1
                
            return curr_sum, curr_count

        dfs(root)
        return count