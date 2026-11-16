# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        lowest = root
        while lowest:
            if p.val < lowest.val and q.val < lowest.val:
                lowest = lowest.left
            elif p.val > lowest.val and q.val > lowest.val:
                lowest = lowest.right
            else:
                return lowest
        