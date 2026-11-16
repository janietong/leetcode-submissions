# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {None: 0}
        
        def dfs(node):
            if node in dp:
                return dp[node]

            maxSum = node.val

            if node.left:
                maxSum += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                maxSum += dfs(node.right.left) + dfs(node.right.right)
            maxSum = max(dfs(node.left) + dfs(node.right), maxSum)
            dp[node] = maxSum
            return maxSum
        return dfs(root)

