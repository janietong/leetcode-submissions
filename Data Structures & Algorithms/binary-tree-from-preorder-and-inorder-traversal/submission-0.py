# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        prei = 0
        ini = 0

        def dfs(limit):
            nonlocal prei, ini
            if prei >= len(preorder):
                return None
            if inorder[ini] == limit:
                ini += 1
                return None
            
            root = TreeNode(preorder[prei])
            prei += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float("inf"))
        