class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
            
        traverse(root)
        return result