class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0
        
        pre = [0 for _ in range(n)]
        next = [0 for _ in range(n)]
        for k in edges:
            pre[k[0]] += 1
            next[k[1]] += 1
            
        
        cnt = 0
        index = -1
        for i in range(n):
            # if not connected
            if pre[i] == 0 and next[i] == 0:
                return -1
            
            # if the strongest
            if next[i] == 0:
                cnt += 1
                index = i
            
        if cnt == 1:
            return index
        else:
            return -1