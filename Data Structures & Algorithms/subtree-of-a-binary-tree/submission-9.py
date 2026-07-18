class Solution:
    def isSubtree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def same(a,b):
            if not a and not b:
                return True

            if not a or not b:
                return False

            return (
                a.val == b.val
                and same(a.left,b.left)
                and same(a.right,b.right)
            )

        def dfs(node):
            if not node:
                return False

            if same(node,q):
                return True

            return dfs(node.left) or dfs(node.right)

        return dfs(p)