class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        queue = []
        # get init
        for i in range(m):
            for k in range(n):
                if matrix[i][k] == 0:
                    queue.append((i, k))

        # set 0
        for q in queue:
            for i in range(m):
                matrix[i][q[1]] = 0

            for i in range(n):
                matrix[q[0]][i] = 0
                

        