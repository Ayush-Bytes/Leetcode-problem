class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty_cells = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    digit = int(board[r][c])
                    mask = 1 << digit
                    b = (r // 3) * 3 + (c // 3)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[b] |= mask

        def backtrack(index: int) -> bool:
            if index == len(empty_cells):
                return True
            
            r, c = empty_cells[index]
            b = (r // 3) * 3 + (c // 3)
            
            used = rows[r] | cols[c] | boxes[b]
            
            for digit in range(1, 10):
                mask = 1 << digit
                if not (used & mask):
                    board[r][c] = str(digit)
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[b] |= mask
                    
                    if backtrack(index + 1):
                        return True
                    
                    board[r][c] = '.'
                    rows[r] ^= mask
                    cols[c] ^= mask
                    boxes[b] ^= mask

            return False

        backtrack(0)