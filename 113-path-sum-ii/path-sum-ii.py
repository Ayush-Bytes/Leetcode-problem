class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []
        
        def dfs(node, current_path, remaining_sum):
            if not node:
                return
            
            current_path.append(node.val)
            
            if not node.left and not node.right and remaining_sum == node.val:
                result.append(list(current_path)) 
            else:
                # Recurse on left and right children
                dfs(node.left, current_path, remaining_sum - node.val)
                dfs(node.right, current_path, remaining_sum - node.val)
                
            # Backtrack by removing the current node before returning to the parent
            current_path.pop()
            
        dfs(root, [], targetSum)
        return result