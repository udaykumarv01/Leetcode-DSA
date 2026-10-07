class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        m = defaultdict(int)
        cont = 0

        for row in grid :
            m[str(row)] += 1

        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cont += m[str(col)]
        return cont