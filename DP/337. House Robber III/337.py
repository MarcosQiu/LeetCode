# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root):
        largest_with_root = dict()
        largest_without_root = dict()

        def dfs(t):
            if t is None:
                return
            dfs(t.left)
            dfs(t.right)
            largest_with_root[id(t)] = t.val + largest_without_root.get(id(t.left), 0) + largest_without_root.get(id(t.right), 0)
            largest_without_root[id(t)] = max(
                largest_with_root.get(id(t.left), 0),
                largest_without_root.get(id(t.left), 0)
            ) + max(
                largest_with_root.get(id(t.right), 0),
                largest_without_root.get(id(t.right), 0)
            )

        dfs(root)
        return max(
            largest_with_root.get(id(root), 0),
            largest_without_root.get(id(root), 0)
        )
