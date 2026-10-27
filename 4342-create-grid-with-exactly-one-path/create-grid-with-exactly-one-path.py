class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        for i in range(m):
            if i == 0:
                # First row completely open
                grid.append('.' * n)
            else:
                # Other rows have obstacles everywhere except the last column
                grid.append('#' * (n - 1) + '.')
        return grid