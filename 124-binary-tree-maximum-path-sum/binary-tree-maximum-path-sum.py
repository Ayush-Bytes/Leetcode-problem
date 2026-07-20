class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Sabse choti possible value se initialize karein
        self.max_sum = float("-inf")
        
        def dfs(node):
            if not node:
                return 0
            
            # Agar left ya right se sum negative aaye, toh use 0 lelein (ignore karein)
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))
            
            # Is current node ko peak/root banakar banane wala max path sum update karein
            current_path_sum = node.val + left_sum + right_sum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Parent node ko sirf ek hi side ka max sum bhej sakte hain
            return node.val + max(left_sum, right_sum)
        
        dfs(root)
        return self.max_sum