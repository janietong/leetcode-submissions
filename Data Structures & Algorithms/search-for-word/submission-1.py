class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i] or (r, c) in seen:
                return False
            
            seen.add((r, c))
            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c

                if dfs(nr, nc, i + 1):
                    return True
            seen.remove((r, c))
            return False
        

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False