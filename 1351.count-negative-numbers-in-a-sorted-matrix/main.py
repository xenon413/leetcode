class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        flat = [item for sublist in grid for item in sublist]
        cnt = 0
        for i in flat:
            if i < 0:
                cnt+=1
        
        return cnt