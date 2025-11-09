class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        row=r-1
        col=0
        
        while col<c and row>=0:
            if matrix[row][col]>target:
                row-=1
            elif matrix[row][col]<target:
                col+=1
            else:
                return True
        return False