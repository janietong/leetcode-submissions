class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        posDiag = set()
        negDiag = set()

        def dfs(r, cur):
            if r == n:
                res.append(["".join(row) for row in cur])
                return

            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                cur[r][c] = "Q"
                dfs(r+1, cur)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                cur[r][c] = "."

        dfs(0, [["."] * n for _ in range(n)])
        return res