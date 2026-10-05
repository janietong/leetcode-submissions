class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(l, r, cur):
            if l == r and l == n:
                res.append("".join(cur[:]))
                return
            
            if l < n:
                cur.append("(")
                dfs(l + 1, r, cur)
                cur.pop()
                
            if r < l:
                cur.append(")")
                dfs(l, r + 1, cur)
                cur.pop()
 
        dfs(0, 0, [])
        return res
            
