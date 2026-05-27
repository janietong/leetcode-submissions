class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(left, right, cur):
            if left == right and left == n:
                result.append("".join(cur))
                return
            
            if left < n:
                cur.append("(")
                dfs(left + 1, right, cur)
                cur.pop()
            if right < left:
                cur.append(")")
                dfs(left, right + 1, cur)
                cur.pop()
        dfs(0, 0, [])
        return result
            