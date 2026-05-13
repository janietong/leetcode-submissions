class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(len(board)):
            seen = set()
            for c in range(len(board)):
                if board[r][c] != "." and board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        
        for c in range(len(board)):
            seen = set()
            for r in range(len(board)):
                if board[r][c] != "." and board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        
        for i in range(9):
            seen = set()
            for row in range(3):
                for col in range(3):
                    r = (i // 3) * 3 + row
                    c = (i % 3) * 3 + col
                    if board[r][c] != "." and board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
        
        return True

