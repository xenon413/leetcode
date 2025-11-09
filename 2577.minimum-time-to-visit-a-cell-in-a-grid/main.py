class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # case: no path
        if grid[1][0] > 1 and grid[0][1] >1:
            return -1

        h, w = len(grid), len(grid[0])
        queue = [(0, 0, 0)]
        been = [[0 for _ in range(w)] for _ in range(h)]
        
        while queue:
            t, x, y = heapq.heappop(queue)
            if x == h-1 and y == w-1:
                return t
            
            if been[x][y] == 1:
                continue
            
            been[x][y] = 1

            next = [[x+1, y], [x-1, y], [x,y+1], [x, y-1]]
            for n in next:
                if 0<=n[0]<h and 0<=n[1]<w and been[n[0]][n[1]]!=1:
                    if t+1 >= grid[n[0]][n[1]]:
                        next_val = t+1
                    else:
                        next_val = grid[n[0]][n[1]]+(grid[n[0]][n[1]] - t+1)%2
                    heapq.heappush(queue, (next_val, n[0], n[1]))
            
        return -1