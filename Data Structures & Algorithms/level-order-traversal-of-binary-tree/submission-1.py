# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            n = len(q)
            temp = []
            for _ in range(n):
                curr = q.pop(0)
                # print(curr.val)
                temp.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            ans.append(temp)
        return ans