# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(stack, node, want):
            if not node:
                return None
            
            stack.append(node)

            if node.val == want:
                return stack
            
            if dfs(stack, node.left, want):
                return stack
            if dfs(stack, node.right, want):
                return stack
            
            stack.pop()
            return None

        pStack = dfs([], root, p.val)
        qStack = dfs([], root, q.val)
        n = min(len(pStack), len(qStack))
        
        lca = None
        for i in range(n):
            if pStack[i] == qStack[i]:
                lca = pStack[i]
        return lca
        


        