# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def good(node, maxVal):
            if not node:
                return 0
            
            if node.val >= maxVal:
                result = 1
                maxVal = node.val
            else:
                result = 0
            
            result += good(node.right, maxVal)
            result += good(node.left, maxVal)
            return result
        return good(root, root.val)
            