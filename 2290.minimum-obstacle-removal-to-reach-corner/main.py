class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        removes = [[-1 for _ in grid[0]] for _ in grid]
        queue = [[0, 0]]
        removes[0][0] = 0
        while queue:
            x, y = queue.pop(0)
            move = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
            for m in move:
                # if in ramge
                if 0<=m[0]<len(grid) and 0<=m[1]<len(grid[0]):
                    new_val = removes[x][y] + grid[m[0]][m[1]]
                    if removes[m[0]][m[1]] == -1 or removes[m[0]][m[1]] > new_val:
                        removes[m[0]][m[1]] = removes[x][y] + grid[m[0]][m[1]]
                        queue.append(m)

        return removes[-1][-1]