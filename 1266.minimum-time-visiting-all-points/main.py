class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        cur_node = points.pop(0)
        cnt = 0
        while points:
            next_node = points.pop(0)
            cnt += abs(cur_node[0]-next_node[0])+abs(cur_node[1]-next_node[1]) - min(abs(cur_node[0]-next_node[0]), abs(cur_node[1]-next_node[1]))
            cur_node = next_node
        return cnt
