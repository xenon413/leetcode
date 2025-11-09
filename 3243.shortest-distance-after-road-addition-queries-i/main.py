class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        neighbors = [[x+1] for x in range(n-1)]
        length = [x for x in range(n)]
        ans = []
        # add neighbors
        for q in queries:
            neighbors[q[0]].append(q[1])

            queue = [q[0]]
            while queue:
                cur = queue.pop(0)
                # find next
                for i in neighbors[cur]:
                    # if closer update and add to queue
                    if length[i]>length[cur]+1:
                        length[i] = length[cur]+1
                        # last index break
                        if i < n-1:
                            queue.append(i)
            ans.append(length[-1])
        return ans
        
        

    