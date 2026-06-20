class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfs(node):
            if not node:
                return

            # Root
            res.append(node.val)

            # Left
            dfs(node.left)

            # Right
            dfs(node.right)

        dfs(root)

        return res